# Plugin pack pages

Generates the pages of the *Monitoring Plugin Packs* docs (`monitoringplugins/`) from the plugin-pack portal DB
and the centreon-plugins sources.

| File | |
|---|---|
| `update-release.mjs` | Brings the docs to a release: regenerates the packs of `packs.json`, adds packs, fetches images, adds release notes, reports new/removed packs and missing sidebar entries |
| `packs.json` | Manifest: documented release, centreon-plugins sources (base ref + overlay branches), technologies, one entry per generated pack |
| `lib.mjs` | Portal DB access through a local build of [i-vertix-pluginpack-mcp](../../../i-vertix-pluginpack-mcp), images through the shared MCP server |
| `fetch-pack.mjs` | Writes the JSON of one plugin pack (description, host/service templates with macros, commands, changelog) |
| `genpage.py` | Renders the MDX page from that JSON |
| `plugininfo.py` | Reads option help (POD) and metrics (perfdata) of a plugin mode from centreon-plugins, starting from a command line |
| `prerequisites/*.md` | Content of the *Prerequisites* section, shared by the packs of one technology (absolute links only) |

The Claude Code skill `.claude/skills/pluginpack-docs-release` describes the whole release workflow.

## Requirements

- `../i-vertix-pluginpack-mcp`, built (`npm run build`) and with a `.env` giving read access to the portal DB (or set `IVERTIX_MCP_DIR`)
- `IVERTIX_MCP_TOKEN` (bearer token of the MCP server, for the images; `IVERTIX_MCP_URL` defaults to `https://10.10.100.112:3100/mcp`)
- `../centreon-plugins` (or `CENTREON_PLUGINS_REPO`): `update-release.mjs` runs `git fetch` and exports `plugins.base` plus the
  `plugins.overlays` of `packs.json` (i-Vertix branches not yet merged into `develop`) to a temp folder; the checkout itself is not touched
- Python 3 (`PYTHON`, default `python`), Node.js ≥ 20

## Release workflow

```bash
node scripts/pluginpacks/update-release.mjs --dry-run           # report only
node scripts/pluginpacks/update-release.mjs                     # newest published release
node scripts/pluginpacks/update-release.mjs --version open      # release in preparation (packs get "open": true)
node scripts/pluginpacks/update-release.mjs --new               # also generate the packs that are new in the release
node scripts/pluginpacks/update-release.mjs --pack "Azure MySQL" --pack 258   # generate/regenerate single packs
```

Options: `--no-fetch` (no `git fetch` in centreon-plugins), `--skip-notes` (leave the release notes page alone).

- A pack is identified by its `unique_id`. The portal DB can be rebuilt, which reassigns `unique_id`s: a pack whose name no
  longer matches `packs.json` is skipped with a warning; correct its `unique_id` in `packs.json` (or pass `--pack <id>` for a real rename).
- New pages go to an existing placeholder with the same slug, otherwise to `<category folder>[/<technology folder>]/<slug>.mdx`;
  a generated `.mdx` replaces the placeholder `.md`. Add new pages to `monitoringplugins_sidebars/sidebar.yaml` (the report lists them)
  and run `node scripts/build-sidebar.js --docs=monitoringplugins`.
- Release notes of published releases newer than the newest entry of `monitoring-plugins/release-notes.md` are prepended.
- Do not run `npm run build` while the dev server runs: both write `.docusaurus/`.

## Single page by hand

```bash
node scripts/pluginpacks/fetch-pack.mjs "Azure MySQL" > azure-mysql.json
python -I scripts/pluginpacks/genpage.py azure-mysql.json monitoringplugins/cloud/azure/azure-mysql.mdx     --image ../../assets/pluginpacks/Databases/Azure-MySQL.png     --prerequisites scripts/pluginpacks/prerequisites/azure.md     --host-macro-hint "e.g. the Azure credentials and the resource to monitor"     --plugins-src <centreon-plugins src folder>
```

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
Metrics are read from the plugin mode (`get_metrics_mapping`, `set_counters*` including entries built in `foreach` loops over
literal lists, `perfdata_add`); modes that only check a status or build their metric names at runtime show no metrics.
