"""Extracts option help (POD) and metrics (perfdata) of a centreon-plugins mode, starting from a command line.

    info = plugin_info(repo_src, command_line)
    info['macro_options']   {'SERVICEWARNING-CPU-USAGE': 'warning-cpu-usage', ...}  (scope+name -> option)
    info['option_help']     {'warning-cpu-usage': 'Warning threshold for CPU percent', ...}
    info['metrics']         [{'name', 'unit', 'description', 'label'}]
"""
import os
import re

OPTION_MACRO = re.compile(r"--([A-Za-z0-9][\w-]*)[= ]['\"]?\$_(HOST|SERVICE)([A-Za-z0-9_.-]+)\$")
GENERIC_PODS = ['centreon/plugins/mode.pm', 'centreon/plugins/templates/counter.pm', 'centreon/plugins/output.pm',
                'centreon/plugins/script_custom.pm', 'centreon/plugins/script_simple.pm', 'centreon/plugins/script_snmp.pm',
                'centreon/plugins/snmp.pm', 'centreon/plugins/http.pm', 'centreon/plugins/ssh.pm', 'centreon/plugins/wsman.pm',
                'centreon/plugins/dbi.pm', 'centreon/plugins/script_sql.pm', 'centreon/plugins/script_wsman.pm']
GENERIC_POD_DIRS = ['centreon/plugins/backend/http', 'centreon/plugins/backend/ssh']


def _read(path):
    try:
        with open(path, encoding='utf-8', errors='replace') as f:
            return f.read()
    except OSError:
        return None


def _pkg_path(src, pkg):
    return os.path.join(src, *pkg.split('::')) + '.pm'


def _pod_inline(text):
    text = re.sub(r'C<<\s*(.*?)\s*>>', r'`\1`', text, flags=re.S)
    text = re.sub(r'C<([^<>]*(?:<[^<>]*>[^<>]*)*)>', r'`\1`', text)
    text = re.sub(r'[BIEFLS]<([^<>]*)>', r'\1', text)
    return re.sub(r'\s+', ' ', text).strip()


def parse_pod_items(code):
    """{'option-name': 'help text'} for every '=item B<--option>' (several B<--x> on one item share the text)."""
    items = {}
    if not code or '__END__' not in code and '=item' not in code:
        return items
    pod = code.split('__END__', 1)[-1] if '__END__' in code else code
    for m in re.finditer(r'^=item\s+(.+?)\n(.*?)(?=^=(?:item|back|head\d|cut))', pod, flags=re.S | re.M):
        names = re.findall(r'--([\w*\[\]-]+)', m.group(1))
        text = _pod_inline(m.group(2))
        for n in names:
            items.setdefault(n, text)
    return items


def _base_classes(code):
    bases = []
    for m in re.finditer(r'use\s+(?:base|parent)\s+(?:-norequire,\s*)?(?:qw\s*[(\[{]\s*([^)\]}]+)[)\]}]|[\'"]([\w:]+)[\'"])', code or ''):
        bases += (m.group(1) or m.group(2)).split()
    return [b for b in bases if '::' in b]


def _class_chain(src, pkg, seen=None):
    """pkg and all its base classes (depth first), as (pkg, code)."""
    seen = seen if seen is not None else set()
    if pkg in seen:
        return []
    seen.add(pkg)
    code = _read(_pkg_path(src, pkg))
    if code is None:
        return []
    chain = [(pkg, code)]
    for base in _base_classes(code):
        chain += _class_chain(src, base, seen)
    return chain


def _hash_entries(block):
    """Top-level "'key' => { ... }" entries of a Perl hash literal."""
    out = []
    for m in re.finditer(r"['\"]?([\w-]+)['\"]?\s*=>\s*\{", block):
        depth, i = 1, m.end()
        while i < len(block) and depth:
            depth += {'{': 1, '}': -1}.get(block[i], 0)
            i += 1
        out.append((m.group(1), block[m.end():i - 1]))
    return out


def _value(body, key):
    m = re.search(r"['\"]?%s['\"]?\s*=>\s*['\"]([^'\"]*)['\"]" % re.escape(key), body)
    return m.group(1) if m else None


def _metrics_from_mapping(code):
    """Azure/AWS style: sub get_metrics_mapping { my $metrics_mapping = { 'x' => { output, label, nlabel, unit } } }."""
    m = re.search(r'sub\s+get_metrics_mapping\s*\{(.*?)\n\}', code, flags=re.S)
    if not m:
        return []
    block = m.group(1)
    start = block.find('{', block.find('='))
    metrics = []
    for _, body in _hash_entries(block[start + 1:]):
        nlabel = _value(body, 'nlabel')
        if not nlabel:
            continue
        metrics.append({'name': nlabel, 'unit': _value(body, 'unit') or '', 'description': _value(body, 'output') or '',
                        'label': _value(body, 'label')})
    return metrics


def _metrics_from_counters(code):
    """Counter template style: set_counters entries { label => 'x', nlabel => 'a.b', set => { perfdatas => [ { unit => '%' } ] } }."""
    # set_counters and helpers such as set_counters_traffic (snmp_standard::mode::interfaces)
    body = ''.join(m.group(1) for m in re.finditer(r'sub\s+set_counters\w*\s*\{(.*?)\n\}', code, flags=re.S))
    metrics = []
    for chunk in re.split(r'\{\s*label\s*=>', body)[1:]:
        label = re.match(r"\s*['\"]([^'\"]+)['\"]", chunk)
        nlabel = re.search(r"nlabel\s*=>\s*['\"]([^'\"]+)['\"]", chunk)
        if not nlabel:
            continue
        unit = re.search(r"perfdatas\s*=>.*?unit\s*=>\s*['\"]([^'\"]*)['\"]", chunk, flags=re.S)
        tpl = re.search(r"output_template\s*=>\s*['\"]([^'\"]*)['\"]", chunk)
        desc = re.sub(r'%[-+ 0-9.]*[a-z]', '', tpl.group(1)).strip(' :') if tpl else ''
        metrics.append({'name': nlabel.group(1), 'unit': unit.group(1) if unit else '', 'description': desc,
                        'label': label.group(1) if label else None})
    return metrics


def _metrics_from_perfdata_add(code):
    metrics = []
    for m in re.finditer(r'perfdata_add\s*\((.*?)\);', code, flags=re.S):
        nlabel = re.search(r"nlabel\s*=>\s*['\"]([^'\"$]+)['\"]", m.group(1))
        if not nlabel:
            continue
        unit = re.search(r"unit\s*=>\s*['\"]([^'\"]*)['\"]", m.group(1))
        metrics.append({'name': nlabel.group(1), 'unit': unit.group(1) if unit else '', 'description': '', 'label': None})
    return metrics


# centreon-plugins naming convention: the last segment of an nlabel names its unit
NLABEL_UNITS = {
    'percentage': '%', 'bytes': 'B', 'bitspersecond': 'b/s', 'bytespersecond': 'B/s', 'persecond': '/s',
    'seconds': 's', 'milliseconds': 'ms', 'microseconds': 'us', 'celsius': 'C', 'volt': 'V', 'watt': 'W',
    'ampere': 'A', 'hertz': 'Hz', 'dbm': 'dBm', 'rpm': 'rpm', 'voltampere': 'VA', 'packetspersecond': 'packets/s',
}


def unit_from_nlabel(nlabel):
    return NLABEL_UNITS.get(nlabel.rsplit('.', 1)[-1], '')


def plugin_info(src, command_line):
    info = {'plugin': None, 'mode': None, 'macro_options': {}, 'option_help': {}, 'metrics': []}
    if not command_line:
        return info
    for m in OPTION_MACRO.finditer(command_line):
        info['macro_options'].setdefault(m.group(2) + m.group(3), m.group(1))
    plugin = re.search(r'--plugin=([\w:]+)', command_line)
    mode = re.search(r'--mode=([\w-]+)', command_line)
    custommode = re.search(r'--custommode=([\w-]+)', command_line)
    if not plugin or not mode:
        return info
    info['plugin'], info['mode'] = plugin.group(1), mode.group(1)
    plugin_code = _read(_pkg_path(src, plugin.group(1))) or ''

    def mapped(kind, key):
        m = re.search(r"['\"]%s['\"]\s*=>\s*['\"]([\w:]+)['\"]" % re.escape(key), plugin_code) if kind == 'mode' else \
            re.search(r"custom_modes\}?->\{['\"]?%s['\"]?\}\s*=\s*['\"]([\w:]+)['\"]" % re.escape(key), plugin_code)
        return m.group(1) if m else None

    mode_pkg = mapped('mode', mode.group(1))
    if not mode_pkg:
        return info
    files = _class_chain(src, mode_pkg)
    if custommode:
        customs = [mapped('custom', custommode.group(1))]
    else:
        # no --custommode: the plugin uses its default one; take all it declares
        customs = re.findall(r"custom_modes\}?(?:->)?\{['\"]?[\w-]+['\"]?\}\s*=\s*['\"]([\w:]+)['\"]", plugin_code)
    for pkg in customs:
        if pkg:
            files += _class_chain(src, pkg)
    files.append((plugin.group(1), plugin_code))
    files += [(p, _read(os.path.join(src, p))) for p in GENERIC_PODS]
    for d in GENERIC_POD_DIRS:
        full = os.path.join(src, d)
        if os.path.isdir(full):
            files += [(f, _read(os.path.join(full, f))) for f in sorted(os.listdir(full)) if f.endswith('.pm')]

    for _, code in files:
        for name, text in parse_pod_items(code).items():
            info['option_help'].setdefault(name, text)

    # metrics of the mode and its base classes (e.g. snmp_standard::mode::interfaces), first definition wins
    metrics, names = [], set()
    for _, code in _class_chain(src, mode_pkg):
        for x in _metrics_from_mapping(code) + _metrics_from_counters(code) + _metrics_from_perfdata_add(code):
            if x['name'] not in names:
                names.add(x['name'])
                if not x['unit']:
                    x['unit'] = unit_from_nlabel(x['name'])
                metrics.append(x)
    info['metrics'] = metrics
    return info


def option_description(info, option):
    """Help text of one option; resolves --warning-*/--critical-* style wildcards."""
    help_ = info['option_help']
    m = re.match(r'(warning|critical)-(.+)$', option)
    # bare "Thresholds." / "Warning threshold." texts are replaced by a text naming the metric
    if option in help_ and not (m and re.fullmatch(r'(?:warning |critical )?thresholds?\.?', help_[option], flags=re.I)):
        return help_[option]
    if m:
        kind, label = m.groups()
        metric = next((x for x in info['metrics'] if x['label'] == label), None)
        what = metric['description'] if metric and metric['description'] else label
        unit = f" ({metric['unit']})" if metric and metric['unit'] else ''
        for key in (f'{kind}-*', f'{kind}-[*]', f'{kind}-[counter]'):
            if key in help_:
                return f'{kind.capitalize()} threshold for {what}{unit}'
        if metric:
            return f'{kind.capitalize()} threshold for {what}{unit}'
    return None
