// Writes the get_plugin_pack JSON of one plugin pack (all sections, plus its changelog from
// get_plugin_pack_changelog under "changelog") to stdout, using the query layer of a
// local, built checkout of the ivertix-pluginpack-mcp server (read-only DB access via its .env).
//
//   node scripts/pluginpacks/fetch-pack.mjs <unique_id | name> [version] > pack.json
//
// The MCP checkout is taken from $IVERTIX_MCP_DIR or ../ivertix-pluginpack-mcp (next to this repository).
// The same data is available through the MCP tool get_plugin_pack once the server runs the current code.
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");
const mcpDir = process.env.IVERTIX_MCP_DIR ?? path.resolve(repoRoot, "..", "ivertix-pluginpack-mcp");
const load = (file) => import(pathToFileURL(path.join(mcpDir, "dist", file)).href);

const [ref, version] = process.argv.slice(2);
if (!ref) {
    console.error("usage: node scripts/pluginpacks/fetch-pack.mjs <unique_id | name> [version] > pack.json");
    process.exit(2);
}

const { getPluginPack, resolveVersion, SECTIONS } = await load("queries.js");
const { getPluginPackChangelog } = await load("changelog.js");
const { pool, query } = await load("db.js");
try {
    const v = await resolveVersion(version);
    const pack = await getPluginPack(v, /^\d+$/.test(ref) ? { unique_id: Number(ref) } : { name: ref }, SECTIONS);
    // changelog of the published releases up to the requested one
    const changelog = await getPluginPackChangelog(pack.unique_id, { includeOpen: v.status === "open" });
    changelog.entries = changelog.entries.filter((e) => e.version.id <= v.id);
    const [oldest] = await query("SELECT id, plugin_version, config_version FROM version ORDER BY id LIMIT 1");
    console.log(JSON.stringify({ ...pack, changelog: { ...changelog, oldest_version: oldest } }, null, 2));
} finally {
    await pool.end();
}
