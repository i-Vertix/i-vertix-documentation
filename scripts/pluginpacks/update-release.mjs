// Brings the Monitoring Plugin Packs docs to a plugin-pack release:
//   1. exports the centreon-plugins sources (base ref + overlay branches of packs.json) to a temp folder
//   2. regenerates the page of every pack in packs.json, plus the packs given with --pack (and with --new the
//      packs added in the release); missing images are fetched from the MCP server
//   3. adds the release notes of published releases missing on monitoring-plugins/release-notes.md
//   4. records the release in packs.json and prints a report (new / removed packs, missing sidebar entries)
//
//   node scripts/pluginpacks/update-release.mjs [--version latest|open|<version>] [--pack <id|name>]... [--new]
//                                               [--dry-run] [--no-fetch] [--skip-notes]
//
// Needs: built i-vertix-pluginpack-mcp checkout with DB access, IVERTIX_MCP_TOKEN (images), centreon-plugins
// checkout (only read: git fetch + git archive), Python 3 ($PYTHON, default "python").
import { execFileSync, spawnSync } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { closeDb, fetchImage, fetchPack, getReleaseNotes, listPluginPacks, listVersions, repoRoot, resolveVersion } from "./lib.mjs";

const here = path.join(repoRoot, "scripts", "pluginpacks");
const docsDir = path.join(repoRoot, "monitoringplugins");
const assetsDir = path.join(docsDir, "assets", "pluginpacks");
const manifestFile = path.join(here, "packs.json");
const sidebarFile = path.join(repoRoot, "monitoringplugins_sidebars", "sidebar.yaml");
const notesFile = path.join(docsDir, "monitoring-plugins", "release-notes.md");
const CATEGORY_FOLDERS = {
    Application: "applications", Cloud: "cloud", Database: "database", Hardware: "hardware", Network: "network",
    Notification: "notification", "Operating System": "operating-system", Storage: "storage",
};

// ---------------------------------------------------------------------------------------------- arguments
const args = { version: "latest", packs: [], new: false, dryRun: false, fetch: true, notes: true };
for (let i = 2; i < process.argv.length; i++) {
    const a = process.argv[i];
    if (a === "--version") args.version = process.argv[++i];
    else if (a === "--pack") args.packs.push(process.argv[++i]);
    else if (a === "--new") args.new = true;
    else if (a === "--dry-run") args.dryRun = true;
    else if (a === "--no-fetch") args.fetch = false;
    else if (a === "--skip-notes") args.notes = false;
    else {
        console.error(`unknown argument ${a}\n` + fs.readFileSync(fileOf(import.meta.url), "utf8").split("\n").filter((l) => l.startsWith("//")).join("\n"));
        process.exit(2);
    }
}
function fileOf(url) {
    return new URL(url).pathname.replace(/^\/([A-Za-z]:)/, "$1");
}

const manifest = JSON.parse(fs.readFileSync(manifestFile, "utf8"));
const report = { regenerated: [], unchanged: [], added: [], missing: [], newInRelease: [], removedInRelease: [], sidebar: [], warnings: [], notes: [] };
const slug = (name) => name.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
const posix = (p) => p.split(path.sep).join("/");
const git = (repo, ...a) => execFileSync("git", ["-C", repo, ...a], { encoding: "utf8" }).trim();

try {
    const target = await resolveVersion(args.version);
    const open = target.status === "open" ? target : await resolveVersion("open").catch(() => null);
    console.log(`Release: ${target.plugin_version} - ${target.config_version} (id ${target.id}, ${target.status})`);
    if (manifest.release) console.log(`Docs were at: ${manifest.release.plugin_version} - ${manifest.release.config_version} (id ${manifest.release.id})`);

    // ------------------------------------------------------------------------------- packs of the release
    const inTarget = new Map((await listPluginPacks({ versionId: target.id, withDescription: false })).map((p) => [p.unique_id, p]));
    const inOpen = open && open.id !== target.id
        ? new Map((await listPluginPacks({ versionId: open.id, withDescription: false })).map((p) => [p.unique_id, p]))
        : inTarget;
    const previous = manifest.release && manifest.release.id !== target.id
        ? manifest.release
        : (await listVersions(false)).find((v) => v.id < target.id);
    if (previous) {
        const before = new Map((await listPluginPacks({ versionId: previous.id, withDescription: false })).map((p) => [p.unique_id, p]));
        for (const [id, p] of inTarget) if (!before.has(id)) report.newInRelease.push(p);
        for (const [id, p] of before) if (!inTarget.has(id)) report.removedInRelease.push(p);
    }

    // packs requested on the command line / new packs -> manifest entries
    const byName = new Map([...inTarget.values(), ...inOpen.values()].map((p) => [p.name.toLowerCase(), p]));
    const requested = args.packs.map((ref) => {
        const p = /^\d+$/.test(ref) ? inTarget.get(Number(ref)) ?? inOpen.get(Number(ref)) : byName.get(ref.toLowerCase());
        if (!p) throw new Error(`plugin pack "${ref}" not found in release ${target.config_version}` + (open ? ` or open ${open.config_version}` : ""));
        const known = manifest.packs[p.unique_id];
        if (known && known.name !== p.name && !/^\d+$/.test(ref))
            throw new Error(`"${p.name}" has unique_id ${p.unique_id}, which packs.json assigns to "${known.name}" (${known.page}). ` +
                "Fix packs.json first (portal DB rebuilt?), or pass the unique_id to confirm a rename.");
        return p;
    });
    if (args.new) requested.push(...report.newInRelease);
    for (const p of requested) {
        if (manifest.packs[p.unique_id]) continue;
        const entry = { name: p.name, page: proposePage(p), ...(inTarget.has(p.unique_id) ? {} : { open: true }) };
        const tech = Object.entries(manifest.technologies).find(([, t]) => new RegExp(t.match).test(p.name));
        if (tech) entry.technology = tech[0];
        manifest.packs[p.unique_id] = entry;
        report.added.push({ ...entry, unique_id: p.unique_id });
    }

    // ------------------------------------------------------------------------------- plugin sources
    const pluginsSrc = args.dryRun ? null : exportPluginSources();

    // ------------------------------------------------------------------------------- pages
    const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "ivertix-packs-"));
    for (const [uid, entry] of Object.entries(manifest.packs).sort((a, b) => a[1].name.localeCompare(b[1].name))) {
        const id = Number(uid);
        let version = null;
        if (inTarget.has(id)) {
            version = target;
            delete entry.open;
        } else if (entry.open && inOpen.has(id)) version = open;
        if (!version) {
            report.missing.push({ unique_id: id, ...entry });
            continue;
        }
        // unique_ids are only stable as long as the portal DB is not rebuilt: a different name means another
        // pack (or a rename) -> only regenerate when the pack was named with --pack
        const current = (version === target ? inTarget : inOpen).get(id).name;
        if (current !== entry.name && !requested.some((p) => p.unique_id === id)) {
            report.warnings.push(`unique_id ${id} is "${current}" in ${version.config_version}, packs.json says "${entry.name}": ` +
                `page ${entry.page} left as is (rename: --pack ${id}; other pack: fix packs.json)`);
            continue;
        }
        const pageFile = path.join(docsDir, entry.page);
        if (args.dryRun) {
            report.regenerated.push(`${entry.name} (${version.config_version})`);
            continue;
        }
        const pack = await fetchPack(id, version);
        entry.name = pack.name;
        const image = pack.image?.path;
        if (!image) report.warnings.push(`${pack.name}: no image in the portal DB`);
        else if (!fs.existsSync(path.join(assetsDir, image))) {
            const data = await fetchImage(id, version);
            if (data) {
                fs.mkdirSync(path.dirname(path.join(assetsDir, image)), { recursive: true });
                fs.writeFileSync(path.join(assetsDir, image), data);
            } else report.warnings.push(`${pack.name}: image ${image} not available on the MCP server`);
        }
        const json = path.join(tmp, `${id}.json`);
        fs.writeFileSync(json, JSON.stringify(pack));
        const tech = entry.technology ? manifest.technologies[entry.technology] : {};
        const before = fs.existsSync(pageFile) ? fs.readFileSync(pageFile, "utf8").replace(/\r\n/g, "\n") : null;
        fs.mkdirSync(path.dirname(pageFile), { recursive: true });
        const py = spawnSync(process.env.PYTHON ?? "python", [
            "-I", path.join(here, "genpage.py"), json, pageFile,
            "--image", posix(path.relative(path.dirname(pageFile), path.join(assetsDir, image ?? "missing.png"))),
            ...(tech.prerequisites ? ["--prerequisites", path.join(here, tech.prerequisites)] : []),
            ...(tech.host_macro_hint ? ["--host-macro-hint", tech.host_macro_hint] : []),
            "--plugins-src", pluginsSrc,
        ], { encoding: "utf8" });
        if (py.status !== 0) throw new Error(`genpage.py failed for ${pack.name}:\n${py.stderr}`);
        for (const w of String(py.stderr ?? "").split(/\r?\n/).filter((l) => l.startsWith("warning: ")))
            report.warnings.push(`${pack.name}: ${w.slice("warning: ".length)}`);
        // a generated .mdx replaces the "coming soon" placeholder .md
        const placeholder = pageFile.replace(/\.mdx$/, ".md");
        if (placeholder !== pageFile && fs.existsSync(placeholder)) fs.rmSync(placeholder);
        const after = fs.readFileSync(pageFile, "utf8");
        (before === after ? report.unchanged : report.regenerated).push(`${pack.name} (${version.config_version})`);
    }
    fs.rmSync(tmp, { recursive: true, force: true });

    // ------------------------------------------------------------------------------- sidebar check
    const sidebar = fs.readFileSync(sidebarFile, "utf8");
    for (const [, entry] of Object.entries(manifest.packs)) {
        const id = path.basename(entry.page).replace(/\.mdx?$/, "");
        if (!new RegExp(`^\\s*-\\s*(id:\\s*)?${id}\\s*$`, "m").test(sidebar)) report.sidebar.push({ id, label: entry.name, folder: posix(path.dirname(entry.page)) });
    }

    // ------------------------------------------------------------------------------- release notes
    if (args.notes) await updateReleaseNotes(target);

    if (!args.dryRun) {
        manifest.release = target.status === "published" ? target : manifest.release;
        fs.writeFileSync(manifestFile, JSON.stringify(manifest, null, 4) + "\n");
    }
    printReport();
} finally {
    await closeDb();
}

// ---------------------------------------------------------------------------------------------- helpers
function proposePage(p) {
    // an existing page (placeholder) with the pack's slug wins, otherwise category folder (+ technology subfolder)
    const name = slug(p.name);
    const found = findFile(docsDir, `${name}.md`) ?? findFile(docsDir, `${name}.mdx`);
    if (found) return posix(path.relative(docsDir, found)).replace(/\.md$/, ".mdx");
    let folder = CATEGORY_FOLDERS[p.category] ?? slug(p.category);
    const sub = slug(p.name.split(/\s+/)[0]);
    if (fs.existsSync(path.join(docsDir, folder, sub))) folder += `/${sub}`;
    return `${folder}/${name}.mdx`;
}

function findFile(dir, file) {
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
        if (e.isDirectory() && e.name !== "assets") {
            const f = findFile(path.join(dir, e.name), file);
            if (f) return f;
        } else if (e.name === file) return path.join(dir, e.name);
    }
    return null;
}

function exportPluginSources() {
    const { repo, base, overlays = [] } = manifest.plugins;
    const repoDir = path.resolve(repoRoot, process.env.CENTREON_PLUGINS_REPO ?? repo);
    if (args.fetch) git(repoDir, "fetch", "--quiet", "origin");
    const dest = path.join(os.tmpdir(), "ivertix-pluginpacks-src");
    fs.rmSync(dest, { recursive: true, force: true });
    fs.mkdirSync(dest, { recursive: true });
    const extract = (ref, paths) => {
        const tar = path.join(dest, "export.tar");
        execFileSync("git", ["-C", repoDir, "archive", "-o", tar, ref, ...paths]);
        execFileSync("tar", ["-xf", "export.tar"], { cwd: dest });
        fs.rmSync(tar);
    };
    extract(base, ["src"]);
    for (const o of overlays) {
        try {
            git(repoDir, "rev-parse", "--verify", "--quiet", o.ref);
        } catch {
            report.warnings.push(`plugin overlay ${o.ref} does not exist (any more): remove it from packs.json`);
            continue;
        }
        const merged = spawnSync("git", ["-C", repoDir, "merge-base", "--is-ancestor", o.ref, base]).status === 0;
        if (merged) report.warnings.push(`plugin overlay ${o.ref} is merged into ${base}: remove it from packs.json`);
        else extract(o.ref, o.paths);
    }
    console.log(`centreon-plugins: ${base} @ ${git(repoDir, "log", "-1", "--format=%h %cs", base)}` +
        (overlays.length ? ` + ${overlays.length} overlay branch(es)` : ""));
    return path.join(dest, "src");
}

async function updateReleaseNotes(target) {
    let text = fs.readFileSync(notesFile, "utf8").replace(/\r\n/g, "\n");
    const onPage = new Set([...text.matchAll(/<h3 id="([^"]+)">/g)].map((m) => m[1]));
    const anchor = (v) => `${v.plugin_version}-${v.config_version}`.toLowerCase();
    const published = await listVersions(false);
    // entries for releases that are not (or no longer) published
    const known = new Set(published.map(anchor));
    for (const id of onPage) if (!known.has(id)) report.warnings.push(`release notes: "${id}" is on the page but not a published release`);
    const missing = published.filter((v) => v.id <= target.id && !onPage.has(anchor(v)) && v.id > Math.max(0, ...published.filter((p) => onPage.has(anchor(p))).map((p) => p.id)));
    if (!missing.length) return;
    const blocks = [];
    for (const v of missing.sort((a, b) => b.id - a.id)) {
        const [notes] = await getReleaseNotes(String(v.id), 1);
        const body = sections(notes?.changelog_markdown ?? "");
        blocks.push(`<details>\n<summary><h3 id="${anchor(v)}">${v.plugin_version} - ${v.config_version}</h3></summary>\n\n${body}\n\n</details>\n`);
        report.notes.push(`${v.plugin_version} - ${v.config_version}`);
    }
    if (args.dryRun) return;
    // newest entry open, the others closed
    text = text.replace("<details open>", "<details>");
    blocks[0] = blocks[0].replace("<details>", "<details open>");
    const at = text.indexOf("<details");
    text = text.slice(0, at) + blocks.join("\n") + "\n" + text.slice(at);
    fs.writeFileSync(notesFile, text);
}

/** Release notes Markdown of the portal -> page format: "###" -> "####", empty sections left out. */
function sections(md) {
    const parts = md.split(/^### /m).slice(1).map((s) => {
        const [title, ...rest] = s.split("\n");
        return { title: title.trim(), body: rest.join("\n").trim() };
    });
    return parts.filter((s) => s.body).map((s) => `#### ${s.title}\n\n${s.body}`).join("\n\n");
}

function printReport() {
    const list = (title, items, fmt = (x) => x) => {
        if (items.length) console.log(`\n${title} (${items.length}):\n` + items.map((x) => `  - ${fmt(x)}`).join("\n"));
    };
    list(args.dryRun ? "Pages to regenerate (not generated in a dry run)" : "Pages regenerated with changes", report.regenerated);
    list("Pages unchanged", report.unchanged);
    list("Packs added to packs.json", report.added, (x) => `${x.name} (${x.unique_id}) -> ${x.page}${x.open ? " [open release]" : ""}`);
    list("Documented packs missing in the release (page left as is)", report.missing, (x) => `${x.name} (${x.unique_id}) ${x.page}`);
    list("New packs in this release (generate with --new or --pack)", report.newInRelease.filter((p) => !manifest.packs[p.unique_id]), (p) => `${p.name} (${p.unique_id}, ${p.category})`);
    list("Packs removed in this release", report.removedInRelease, (p) => `${p.name} (${p.unique_id})`);
    list("Pages missing in monitoringplugins_sidebars/sidebar.yaml", report.sidebar, (x) => `${x.folder}: - id: ${x.id} / label: ${x.label}`);
    list("Release notes added", report.notes);
    list("Warnings", report.warnings);
    if (args.dryRun) console.log("\n(dry run: nothing written)");
}
