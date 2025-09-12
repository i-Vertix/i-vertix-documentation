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
