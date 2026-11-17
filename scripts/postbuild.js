const fs = require('fs');
const path = require('path');

const outputDir = path.resolve(__dirname, '..', 'build');
const filePath = path.join(outputDir, 'build.json');

if (!fs.existsSync(outputDir)) {
    console.log("Output directory not present");
    process.exit(1);
}

const rootDir = fs.readdirSync(path.resolve(__dirname, '..'), { withFileTypes: true, recursive: false });

const buildJson = {
    timestamp: new Date().getTime()
};

for (const item of rootDir) {
    if (!item.isFile()) continue;
    const matches = item.name.match(/^([a-zA-Z_-]+)_versions\.json$/);
    if (!matches || !matches[1]) continue;

    const versionsFile = path.resolve(__dirname, '..', matches[0]);
    const docId = matches[1];

    const versions = JSON.parse(fs.readFileSync(versionsFile, 'utf8'));

    buildJson[`${docId}Indexes`] = {};

    versions.forEach((version, index) => {
        if (index === 0) {
            buildJson[`${docId}Indexes`][version] = `/search-index-${docId}.json`;
        } else {
            fs.renameSync(
                path.resolve(outputDir, docId, version, `search-index-${docId}.json`),
                path.resolve(outputDir, docId, version, `search-index.json`),
            );
            buildJson[`${docId}Indexes`][version] = `/${docId}/${version}/search-index.json`;
        }
    });
}

fs.writeFileSync(filePath, JSON.stringify(buildJson), 'utf8');

// ------------------------------------------------------------------------------------------------
// Service template index of the Monitoring Plugin Packs: { "<service template name>": "<page url>#<anchor>" }.
// Built from the "### Alias {/* #name */}" headings of the generated plugin pack pages; every entry is
// checked against the built HTML. Names on several pages (e.g. Ping-LAN from generic-host) are left out.
const siteUrl = require('../docusaurus.config.js').url.replace(/\/+$/, '');
const pluginDocsDir = path.resolve(__dirname, '..', 'monitoringplugins');
const indexFile = path.join(outputDir, 'monitoringplugins', 'service-templates.json');

function listPages(dir) {
    return fs.readdirSync(dir, { withFileTypes: true }).flatMap((e) => {
        const full = path.join(dir, e.name);
        if (e.isDirectory()) return e.name === 'assets' ? [] : listPages(full);
        return /\.mdx?$/.test(e.name) ? [full] : [];
    });
}

const found = {};
for (const file of listPages(pluginDocsDir)) {
    const route = '/monitoringplugins/' + path.relative(pluginDocsDir, file).split(path.sep).join('/').replace(/\.mdx?$/, '');
    const content = fs.readFileSync(file, 'utf8');
    const section = content.split(/^## Service Templates\s*$/m)[1];
    if (!section) continue;
    const body = section.split(/^## /m)[0];
    for (const m of body.matchAll(/^### .*\{\/\*\s*#([\w.-]+)\s*\*\/\}\s*$/gm)) {
        (found[m[1]] ??= []).push(route);
    }
}

const serviceTemplates = {};
const skipped = [];
for (const [name, routes] of Object.entries(found).sort(([a], [b]) => a.localeCompare(b))) {
    const pages = [...new Set(routes)];
    if (pages.length > 1) {
        skipped.push(`${name} (${pages.length} pages)`);
        continue;
    }
    const html = path.join(outputDir, ...pages[0].split('/').filter(Boolean), 'index.html');
    if (!fs.existsSync(html) || !new RegExp(`id=["']?${name.replace(/[.]/g, '\\.')}["' >]`).test(fs.readFileSync(html, 'utf8'))) {
        skipped.push(`${name} (anchor not found in ${pages[0]})`);
        continue;
    }
    serviceTemplates[name] = `${siteUrl}${pages[0]}#${name}`;
}

fs.mkdirSync(path.dirname(indexFile), { recursive: true });
fs.writeFileSync(indexFile, JSON.stringify(serviceTemplates, null, 2) + '\n', 'utf8');
console.log(`Service template index: ${Object.keys(serviceTemplates).length} entries -> ${path.relative(path.resolve(__dirname, '..'), indexFile)}`);
if (skipped.length) console.log(`  skipped: ${skipped.join(', ')}`);
