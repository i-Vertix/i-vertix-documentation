# Plugin pack pages

Generates the pages of the *Monitoring Plugin Packs* docs (`monitoringplugins/`) from the plugin-pack portal DB
and the centreon-plugins sources.

| File | |
|---|---|
| `fetch-pack.mjs` | Writes the JSON of one plugin pack (description, host/service templates with macros, commands) using a local build of [i-vertix-pluginpack-mcp](../../../i-vertix-pluginpack-mcp) |
| `genpage.py` | Renders the MDX page from that JSON |
| `plugininfo.py` | Reads option help (POD) and metrics (perfdata) of a plugin mode from centreon-plugins, starting from a command line |
| `prerequisites/*.md` | Content of the *Prerequisites* section, shared by the packs of one technology |

## Requirements

- `../i-vertix-pluginpack-mcp`, built (`npm run build`) and with a `.env` giving read access to the portal DB (or set `IVERTIX_MCP_DIR`)
- `../centreon-plugins` checked out at the plugin version the docs describe (or set `CENTREON_PLUGINS_SRC` to its `src` folder)
- Python 3, Node.js ≥ 20

## Usage

```bash
node scripts/pluginpacks/fetch-pack.mjs "Azure MySQL" > azure-mysql.json
python -I scripts/pluginpacks/genpage.py azure-mysql.json monitoringplugins/cloud/azure/azure-mysql.mdx \
    --image ../../assets/pluginpacks/Databases/Azure-MySQL.png \
    --prerequisites scripts/pluginpacks/prerequisites/azure.md \
    --host-macro-hint "e.g. the Azure credentials and the resource to monitor"
```

The image comes from the plugin store media folder (`image.path` in the JSON); copy it to
`monitoringplugins/assets/pluginpacks/<path>`.

## What the page contains

- Header (image, name, category, metadata) via `src/components/PluginPackHeader`
- Description, Prerequisites
- Per host template: macros, and its service templates in two tabs (linked to the host template / other service templates of the pack)
- Per service template (collapsed `<details>`, opened by `src/clientModules/openDetailsOnHash.js` when its anchor is targeted): macros and metrics
- Changelog: one collapsible section per release (newest open). It comes from `getPluginPackChangelog` of the MCP checkout
  (tool `get_plugin_pack_changelog`), which compares the pack between consecutive releases via the `unique_id` of its objects
  (pack, host templates, the service templates and commands it owns) and adds `breaking_change` entries. Service templates
  inherited from other packs' host templates (e.g. `Ping-LAN` from `generic-host`) are left out.

Macro descriptions come from the portal DB; missing ones are taken from the help of the plugin option the macro is passed to.
Metrics are read from the plugin mode (`get_metrics_mapping`, `set_counters*`, `perfdata_add`); modes that only check a
status or build their metric names at runtime show no metrics.
