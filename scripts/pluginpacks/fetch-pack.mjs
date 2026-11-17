// Writes the get_plugin_pack JSON of one plugin pack (all sections, plus its changelog from
// get_plugin_pack_changelog under "changelog") to stdout, see lib.mjs for the data source.
//
//   node scripts/pluginpacks/fetch-pack.mjs <unique_id | name> [version] > pack.json
//
// The same data is available through the MCP tool get_plugin_pack once the server runs the current code.
import { closeDb, fetchPack, resolveVersion } from "./lib.mjs";

const [ref, version] = process.argv.slice(2);
if (!ref) {
    console.error("usage: node scripts/pluginpacks/fetch-pack.mjs <unique_id | name> [version] > pack.json");
    process.exit(2);
}

try {
    console.log(JSON.stringify(await fetchPack(ref, await resolveVersion(version)), null, 2));
} finally {
    await closeDb();
}
