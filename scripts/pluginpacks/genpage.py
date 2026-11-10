"""Renders a plugin pack page (MDX) from the get_plugin_pack JSON of the ivertix-pluginpacks MCP server,
completed with the centreon-plugins sources.

- macro descriptions: plugin pack DB first, otherwise the help (POD) of the plugin option the macro is passed to
- metrics: perfdata of the plugin mode (get_metrics_mapping / set_counters / perfdata_add)

Example:
    python -I scripts/pluginpacks/genpage.py pack.json monitoringplugins/cloud/azure/azure-mysql.mdx \
        --image ../../assets/pluginpacks/Databases/Azure-MySQL.png \
        --prerequisites prerequisites.md --host-macro-hint "e.g. the Azure credentials and the resource to monitor"

The centreon-plugins checkout is taken from --plugins-src, $CENTREON_PLUGINS_SRC or ../centreon-plugins/src
(next to this repository).
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plugininfo import plugin_info, option_description  # noqa: E402

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# macros that are not bound to a plugin option but appended to the command line as they are
FREE_MACROS = {
    'EXTRA-OPTS': 'Additional options appended to the plugin command line (host level).',
    'EXTRAOPTS': 'Additional options appended to the plugin command line (service level).',
}


# collapsible section without the light-blue alert look of <details>, see src/css/custom.css
DETAILS_OPEN = '<details className="plugin-pack-details">'


def bare(name):
    return re.sub(r'^\$_(HOST|SERVICE)', '', name).strip('$')


def cell(text):
    """Escapes text for a Markdown table cell inside MDX (code spans stay literal)."""
    if not text:
        return ''
    text = text.replace('\r', '').replace('\n', ' ')
    parts = re.split(r'(`[^`]*`)', text)
    for i, part in enumerate(parts):
        if part.startswith('`') and part.endswith('`') and len(part) > 1:
            parts[i] = part.replace('|', '\\|')
        else:
            parts[i] = part.replace('|', '\\|').replace('<', '&lt;').replace('{', '\\{').replace('}', '\\}')
    return ''.join(parts).strip()


def inline(text):
    """Escapes text for MDX outside tables (code spans stay literal)."""
    if not text:
        return ''
    parts = re.split(r'(`[^`]*`)', text.replace('\r', '').replace('\n', ' '))
    return ''.join(p if p.startswith('`') and len(p) > 1 else p.replace('<', '&lt;').replace('{', '\\{').replace('}', '\\}')
                   for p in parts).strip()


def code(value):
    if value is None or value == '':
        return ''
    return '`' + value.replace('|', '\\|') + '`'


def nowrap_table(rows, css_class='plugin-pack-macros'):
    # plugin-pack-macros: first column (macro / metric names) on one line,
    # plugin-pack-templates: template names on one line; see src/css/custom.css
    return f'<div className="{css_class}">\n\n' + '\n'.join(rows) + '\n\n</div>'


class Page:
    def __init__(self, pack, plugins_src):
        self.d = pack
        self.stpls = {s['name']: s for s in pack['service_templates']}
        commands = {c['name']: c for c in pack.get('commands', [])}
        self.command_lines = {name: c['command_line'] or '' for name, c in commands.items()}
        self.infos = {name: plugin_info(plugins_src, c['command_line']) for name, c in commands.items()}

    def used(self, macro, scope, command_names):
        """True if one of the commands passes the macro (unknown commands count as using it)."""
        lines = [self.command_lines[n] for n in command_names if n in self.command_lines]
        if not lines:
            return True
        return any(f'$_{scope}{bare(macro["name"])}$' in line for line in lines)

    def describe(self, macro, scope, command_names):
        """Description of a macro: DB value, else plugin option help of the first command using it."""
        if macro['description'] and macro['description'].strip():
            return macro['description']
        key = scope + bare(macro['name'])
        for name in command_names:
            info = self.infos.get(name)
            if info and key in info['macro_options']:
                text = option_description(info, info['macro_options'][key])
                if text:
                    return text
        return FREE_MACROS.get(bare(macro['name']))

    def macro_table(self, macros, scope, command_names):
        rows = ['| Macro | Default value | Description |', '|-------|---------------|-------------|']
        for m in macros:
            used = self.used(m, scope, command_names)
            if not used and m.get('defined_on') == 'command':
                continue  # stale macro definition of a command that its command line no longer uses
            default = '*(password)*' if m['is_password'] else code(m['default_value'])
            desc = cell(self.describe(m, scope, command_names))
            if not used:
                desc = (desc + ' ' if desc else '') + '*(not used by the check command)*'
            rows.append(f"| `{bare(m['name'])}` | {default} | {desc} |")
        return nowrap_table(rows)

    @staticmethod
    def metric_table(info, macros):
        """Metrics of the plugin mode, with the service macros that set their thresholds."""
        option_macro = {option: key[len('SERVICE'):] for key, option in info['macro_options'].items() if key.startswith('SERVICE')}
        defined = {bare(m['name']) for m in macros}
        rows = ['| Metric | Unit | Description | Threshold macros |', '|--------|------|-------------|------------------|']
        for m in info['metrics']:
            thresholds = [option_macro.get(f'{kind}-{m["label"]}') for kind in ('warning', 'critical')] if m['label'] else []
            thresholds = [f'`{t}`' for t in thresholds if t and t in defined]
            rows.append(f"| `{m['name']}` | {code(m['unit'])} | {cell(m['description'])} | {', '.join(thresholds)} |")
        return nowrap_table(rows)

    def stpl_table(self, entries):
        rows = ['| Service template | Name |', '|------------------|------|']
        for name, inherited_from in entries:
            s = self.stpls.get(name, {'alias': None})
            label = s['alias'] or name
            note = f' (inherited from `{inherited_from}`)' if inherited_from else ''
            rows.append(f"| [{cell(label)}](#{name.lower()}){note} | `{name}` |")
        return nowrap_table(rows, 'plugin-pack-templates')

    def host_service_tabs(self, h):
        linked = [(s['name'], s['inherited_from']) for s in h['service_templates']]
        linked_names = {n for n, _ in linked}
        others = [(n, None) for n in sorted(self.stpls, key=lambda n: (self.stpls[n]['alias'] or n).lower()) if n not in linked_names]
        out = ['<Tabs>', '<TabItem value="linked" label="Linked to the host template" default>', '']
        if linked:
            out += ['These service templates are linked to the host template: the services are created automatically on every host using it.', '',
                    self.stpl_table(linked), '']
        else:
            out += ['*No service templates are linked to this host template.*', '']
        out += ['</TabItem>', '<TabItem value="others" label="Other service templates">', '']
        if others:
            out += ['These service templates are part of the plugin pack, but not linked to the host template. '
                    'Create the services manually or by a service discovery.', '', self.stpl_table(others), '']
        else:
            out += ['*All service templates of the plugin pack are linked to this host template.*', '']
        out += ['</TabItem>', '</Tabs>']
        return out

    def render(self, image_path, prereq, host_hint):
        d = self.d
        lines = [
            '---',
            f'title: "{d["name"]}"',
            'hide_title: true',
            '---',
            '',
            'import PluginPackHeader from "@site/src/components/PluginPackHeader";',
            'import Tabs from "@theme/Tabs";',
            'import TabItem from "@theme/TabItem";',
            f'import image from "{image_path}";',
            '',
            f'<PluginPackHeader name="{d["name"]}" image={{image}} category="{d["category"]}" metadata={{{json.dumps(d["metadata"])}}} />',
            '',
            '## Description',
            '',
            d['description_markdown'].strip(),
            '',
        ]
        if prereq:
            lines += ['## Prerequisites', '', prereq.strip(), '']
        lines += ['## Host Templates', '']

        for h in d['host_templates']:
            lines += [f'### {h["name"]}', '']
            info = [f'*{h["alias"]}*'] if h['alias'] else []
            if h['parent_templates']:
                info.append('Parent template: ' + ', '.join(f'`{p}`' for p in h['parent_templates']))
            if info:
                lines += [' · '.join(info), '']
            # host macros are passed by the commands of the linked service templates
            host_cmds = [h['check_command']] if h['check_command'] else []
            host_cmds += [self.stpls[s['name']]['check_command'] for s in h['service_templates']
                          if s['name'] in self.stpls and self.stpls[s['name']]['check_command']]
            lines += [DETAILS_OPEN, f'<summary>Macros ({len(h["macros"])})</summary>', '',
                      self.macro_table(h['macros'], 'HOST', host_cmds), '']
            if any(m['defined_on'] == 'command' for m in h['macros']):
                lines += [('Macros without a default value are only defined in the check commands. Set them on the host where needed'
                           + (f' ({host_hint})' if host_hint else '') + '.'), '']
            lines += ['</details>', '']
            lines += ['#### Service Templates', ''] + self.host_service_tabs(h) + ['']

        lines += ['## Service Templates', '']
        order = []
        for h in d['host_templates']:
            order += [s['name'] for s in h['service_templates'] if s['name'] not in order]
        order += [n for n in sorted(self.stpls) if n not in order]
        for name in order:
            s = self.stpls[name]
            cmd = s['check_command']
            # collapsed by default; the markdown heading inside <summary> keeps the TOC entry,
            # src/clientModules/openDetailsOnHash.js opens it when its anchor is targeted
            lines += [DETAILS_OPEN, '<summary>', '', f'### {s["alias"] or s["name"]} {{#{s["name"].lower()}}}', '', '</summary>', '']
            info = [f'`{s["name"]}`']
            if cmd:
                info.append(f'Check command: `{cmd}`')
            lines += [' · '.join(info), '']
            if s['macros']:
                lines += ['#### Macros', '', self.macro_table(s['macros'], 'SERVICE', [cmd] if cmd else []), '']
            if cmd and self.infos.get(cmd) and self.infos[cmd]['metrics']:
                lines += ['#### Metrics', '', self.metric_table(self.infos[cmd], s['macros']), '']
            lines += ['</details>', '']

        lines += self.changelog()
        return '\n'.join(lines).rstrip() + '\n', len(order)

    OBJECT_LABELS = {'plugin_pack': 'Plugin pack', 'host_template': 'Host template',
                     'service_template': 'Service template', 'command': 'Command'}

    def changelog(self):
        """Changelog section: one collapsible section per release (newest open), changes grouped by object."""
        cl = self.d.get('changelog')
        if not cl:
            return []
        out = ['## Changelog', '']
        entries = cl.get('entries', [])
        first, oldest = cl.get('first_version'), cl.get('oldest_version')
        label = lambda v: f'{v["plugin_version"]} - {v["config_version"]}'  # noqa: E731  (as in the Plugin Store "Version Overview")
        if not entries:
            if first and oldest and first['id'] == oldest['id']:
                out += [f'No changes since `{label(first)}`, the oldest release in the plugin store history.', '']
            elif first:
                out += [f'No changes since the plugin pack was added in `{label(first)}`.', '']
            return out
        out += ['Changes of the plugin pack per release, compared with the previous release.', '']
        for n, e in enumerate(entries):
            out += [DETAILS_OPEN.replace('>', ' open>') if n == 0 else DETAILS_OPEN, f'<summary>{label(e["version"])}</summary>', '']
            groups = {}
            for c in e['changes']:
                groups.setdefault((c['object'], c['name']), []).append(c['change'])
            for (obj, name), changes in groups.items():
                if obj == 'plugin_pack' and (not name or changes[0].startswith('**Breaking')):
                    out += [f'- {inline(ch)}' for ch in changes]
                    continue
                target = f'[`{name}`](#{name.lower()})' if obj == 'service_template' and name in self.stpls else f'`{name}`'
                out.append(f'- {self.OBJECT_LABELS.get(obj, obj)} {target}')
                out += [f'    - {inline(ch)}' for ch in changes]
            out += ['', '</details>', '']
        if first and oldest and first['id'] != oldest['id']:
            out += [f'The plugin pack was added in `{label(first)}`.', '']
        return out


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('pack_json', help='get_plugin_pack output (all sections)')
    p.add_argument('out', help='MDX file to write')
    p.add_argument('--image', required=True, help='image import path, relative to the MDX file')
    p.add_argument('--prerequisites', help='Markdown file with the content of the Prerequisites section')
    p.add_argument('--host-macro-hint', default='', help='hint appended to the note about host macros without default value')
    p.add_argument('--plugins-src', default=os.environ.get('CENTREON_PLUGINS_SRC', os.path.join(REPO_ROOT, '..', 'centreon-plugins', 'src')),
                   help='src folder of the centreon-plugins checkout')
    a = p.parse_args()

    if not os.path.isdir(a.plugins_src):
        p.error(f'centreon-plugins src folder not found: {a.plugins_src}')
    pack = json.load(open(a.pack_json, encoding='utf-8'))
    prereq = open(a.prerequisites, encoding='utf-8').read() if a.prerequisites else ''
    page = Page(pack, a.plugins_src)
    text, count = page.render(a.image, prereq, a.host_macro_hint)
    with open(a.out, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)
    print(f'written {a.out}: {count} service templates, '
          f'{sum(len(i["metrics"]) for i in page.infos.values())} metrics from {sum(1 for i in page.infos.values() if i["mode"])} plugin modes')


if __name__ == '__main__':
    main()
