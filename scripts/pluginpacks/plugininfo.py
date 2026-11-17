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


def _metrics_from_mapping(code, per_sec=False):
    """Azure/AWS style: sub get_metrics_mapping { my $metrics_mapping = { 'x' => { output, label, nlabel, unit } } }.
    AWS nests the entries under "metrics => { ... }" and gives nlabel per value type
    ("nlabel => { absolute => 'a.count', per_second => 'a.persecond' }"); per_sec picks the --per-sec one."""
    m = re.search(r'sub\s+get_metrics_mapping\s*\{(.*?)\n\}', code, flags=re.S)
    if m:
        block = m.group(1)
        block = block[block.find('{', block.find('=')) + 1:]
    else:
        # older AWS modes: file-level "my %metrics_mapping = ( 'x' => { ... }, ... );"
        m = re.search(r'^my\s+%metrics_mapping\s*=\s*\((.*?)^\);', code, flags=re.S | re.M)
        if not m:
            return []
        block = m.group(1)
    metrics = []
    for _, body in _hash_entries(block):
        if len(re.findall(r"['\"]?\boutput['\"]?\s*=>", body)) != 1:
            continue  # container ("metrics => {...}") or a hash without a metric definition
        nlabel = _value(body, 'nlabel')
        per_second = False
        if not nlabel:
            h = re.search(r"\bnlabel['\"]?\s*=>\s*\{(.*?)\}", body, flags=re.S)
            variants = dict(re.findall(r"(\w+)\s*=>\s*['\"]([^'\"]+)['\"]", h.group(1))) if h else {}
            per_second = per_sec and 'per_second' in variants
            nlabel = variants.get('per_second' if per_second else 'absolute') or next(iter(variants.values()), None)
        if not nlabel:
            continue
        unit = _value(body, 'unit') or ''
        if per_second and unit:
            unit += '/s'
        metrics.append({'name': nlabel, 'unit': unit, 'description': _value(body, 'output') or '',
                        'label': _value(body, 'label')})
    return metrics


def _metrics_from_counters(code):
    """Counter template style: set_counters entries { label => 'x', nlabel => 'a.b', set => { perfdatas => [ { unit => '%' } ] } }."""
    # set_counters and helpers such as set_counters_traffic (snmp_standard::mode::interfaces)
    body = ''.join(m.group(1) for m in re.finditer(r'sub\s+set_counters\w*\s*\{(.*?)\n\}', code, flags=re.S))
    metrics = []
    for chunk in re.split(r'\{\s*label\s*=>', body)[1:]:
        label = re.match(r"\s*['\"]([^'\"]+)['\"]", chunk)
        nlabel = re.search(r"nlabel\s*=>\s*['\"]([^'\"]+)['\"](?!\s*\.)", chunk)
        if not nlabel:
            continue
        unit = re.search(r"perfdatas\s*=>.*?unit\s*=>\s*['\"]([^'\"]*)['\"]", chunk, flags=re.S)
        tpl = re.search(r"output_template\s*=>\s*['\"]([^'\"]*)['\"]", chunk)
        desc = re.sub(r'%[-+ 0-9.]*[a-z]', '', tpl.group(1)).strip(' :') if tpl else ''
        metrics.append({'name': nlabel.group(1), 'unit': unit.group(1) if unit else '', 'description': desc,
                        'label': label.group(1) if label else None})
    return metrics


def _perl_str(expr, env):
    """Value of a Perl string expression made of quoted strings, variables of env and lc()/uc() calls joined
    with '.'; None when it contains anything else."""
    funcs = {'lc': str.lower, 'uc': str.upper, 'ucfirst': lambda s: s[:1].upper() + s[1:],
             'lcfirst': lambda s: s[:1].lower() + s[1:]}
    out = []
    for part in re.split(r'\s+\.\s+|\s*\.\s*(?=[\'"$a-z])', expr.strip()):
        part = part.strip()
        if m := re.fullmatch(r"'([^']*)'", part):
            out.append(m.group(1))
        elif m := re.fullmatch(r'"([^"]*)"', part):
            text = m.group(1)
            for var in re.findall(r'\$\{?(\w+)\}?', text):
                if var not in env:
                    return None
            out.append(re.sub(r'\$\{?(\w+)\}?', lambda v: env[v.group(1)], text))
        elif (m := re.fullmatch(r'\$(\w+)', part)) and m.group(1) in env:
            out.append(env[m.group(1)])
        elif (m := re.fullmatch(r'(\w+)\s*\(\s*\$(\w+)\s*\)', part)) and m.group(1) in funcs and m.group(2) in env:
            out.append(funcs[m.group(1)](env[m.group(2)]))
        else:
            return None
    return ''.join(out)


def _metrics_from_counter_loops(code):
    """Counter entries built in nested foreach loops over literal lists (older Azure modes), e.g.
    foreach my $aggregation ('total') { foreach my $metric ('BlobCapacity') { my $metric_label = lc($metric);
    { label => $metric_label . '-' . $aggregation, ... perfdatas => [ { label => $metric_label . '_' . $aggregation } ] } } }."""
    body = ''.join(m.group(1) for m in re.finditer(r'sub\s+set_counters\w*\s*\{(.*?)\n\}', code, flags=re.S))
    loops = list(re.finditer(r"foreach\s+my\s+\$(\w+)\s*\((?:\s*qw\s*\(([^)]*)\)|([^)]*))\)\s*\{", body))
    if not loops:
        return []
    lists = []
    for m in loops:
        items = m.group(2).split() if m.group(2) is not None else re.findall(r"['\"]([^'\"]+)['\"]", m.group(3))
        if not items or (m.group(3) is not None and re.search(r'[$%@]', m.group(3))):
            return []  # loop over a runtime list (e.g. keys of a hash): names unknown
        lists.append((m.group(1), items))
    inner = body[loops[0].end():]
    derived = re.findall(r'my\s+\$(\w+)\s*=\s*([^;]+);', inner)
    entry = re.search(r'label\s*=>\s*([^,]+?)\s*,\s*(?:nlabel\s*=>\s*([^,]+?)\s*,\s*)?set\s*=>', inner)
    perf = re.search(r'perfdatas\s*=>\s*\[\s*\{\s*label\s*=>\s*([^,]+?)\s*,', inner)
    unit = re.search(r"perfdatas\s*=>.*?unit\s*=>\s*['\"]([^'\"]*)['\"]", inner, flags=re.S)
    tpl = re.search(r'output_template\s*=>\s*([^,]+?)\s*,', inner)
    if not entry:
        return []

    def product(i, env):
        if i == len(lists):
            yield dict(env)
            return
        var, items = lists[i]
        for item in items:
            env[var] = item
            yield from product(i + 1, env)

    metrics = []
    for env in product(0, {}):
        for var, expr in derived:
            value = _perl_str(expr, env)
            if value is not None:
                env[var] = value
        label = _perl_str(entry.group(1), env)
        name = (_perl_str(entry.group(2), env) if entry.group(2) else None) or (_perl_str(perf.group(1), env) if perf else None)
        if not name:
            continue
        desc = _perl_str(tpl.group(1), env) if tpl else ''
        desc = re.sub(r'%[-+ 0-9.]*[a-z]', '', desc or '').strip(' :')
        metrics.append({'name': name, 'unit': unit.group(1) if unit else '', 'description': desc, 'label': label})
    return metrics


def _metrics_from_perfdata_add(code):
    metrics = []
    for m in re.finditer(r'perfdata_add\s*\((.*?)\);', code, flags=re.S):
        nlabel = re.search(r"nlabel\s*=>\s*['\"]([^'\"$]+)['\"](?!\s*\.)", m.group(1))
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
            re.search(r"custom_modes\}?(?:->)?\{['\"]?%s['\"]?\}\s*=\s*['\"]([\w:]+)['\"]" % re.escape(key), plugin_code)
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
        for x in (_metrics_from_mapping(code, per_sec=bool(re.search(r'--per-sec\b', command_line))) +_metrics_from_counters(code) + _metrics_from_counter_loops(code)
                  + _metrics_from_perfdata_add(code)):
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
