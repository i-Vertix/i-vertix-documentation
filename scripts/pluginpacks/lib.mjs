// Shared helpers of the plugin pack scripts:
// - plugin-pack portal DB through the query layer of a local, built i-vertix-pluginpack-mcp checkout
//   ($IVERTIX_MCP_DIR or ../i-vertix-pluginpack-mcp next to this repository, read-only DB access via its .env)
// - pack images through the shared MCP server over HTTP ($IVERTIX_MCP_URL, $IVERTIX_MCP_TOKEN), because the
//   image files live only on the portal VM
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

export const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");
export const mcpDir = process.env.IVERTIX_MCP_DIR ?? path.resolve(repoRoot, "..", "i-vertix-pluginpack-mcp");
const load = (file) => import(pathToFileURL(path.join(mcpDir, "dist", file)).href);

const queries = await load("queries.js");
const { getPluginPackChangelog } = await load("changelog.js");
const db = await load("db.js");

export const { resolveVersion, listVersions, listPluginPacks, getReleaseNotes } = queries;
export const closeDb = () => db.pool.end();

/** get_plugin_pack JSON of one pack (all sections) plus its changelog up to `version` under "changelog". */
export async function fetchPack(ref, version) {
    const pack = await queries.getPluginPack(
        version,
        typeof ref === "number" || /^\d+$/.test(ref) ? { unique_id: Number(ref) } : { name: ref },
        queries.SECTIONS,
    );
    // changelog of the published releases up to the requested one
    const changelog = await getPluginPackChangelog(pack.unique_id, { includeOpen: version.status === "open" });
    changelog.entries = changelog.entries.filter((e) => e.version.id <= version.id);
    const [oldest] = await db.query("SELECT id, plugin_version, config_version FROM version ORDER BY id LIMIT 1");
    return { ...pack, changelog: { ...changelog, oldest_version: oldest } };
}

/** Image of a pack as a Buffer (null when the pack has no image), via the MCP tool get_plugin_pack_image. */
export async function fetchImage(uniqueId, version) {
    const url = process.env.IVERTIX_MCP_URL ?? "https://10.10.100.112:3100/mcp";
    const token = process.env.IVERTIX_MCP_TOKEN;
    if (!token) throw new Error("IVERTIX_MCP_TOKEN is not set (bearer token of the plugin pack MCP server)");
    const res = await fetch(url, {
        method: "POST",
        headers: {
            "content-type": "application/json",
            accept: "application/json, text/event-stream",
            authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
            jsonrpc: "2.0",
            id: 1,
            method: "tools/call",
            params: { name: "get_plugin_pack_image", arguments: { unique_id: uniqueId, version: String(version.id) } },
        }),
    });
    if (!res.ok) throw new Error(`MCP server: HTTP ${res.status}`);
    const body = await res.text();
    // Streamable HTTP answers with one SSE "data:" line (or plain JSON)
    const json = JSON.parse(body.split("\n").find((l) => l.startsWith("data:"))?.slice(5) ?? body);
    if (json.error) throw new Error(`MCP server: ${json.error.message}`);
    const image = json.result?.content?.find((c) => c.type === "image");
    return image ? Buffer.from(image.data, "base64") : null;
}
