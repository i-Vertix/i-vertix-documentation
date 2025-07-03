const fs = require('fs');
const path = require('path');

const outputDir = path.resolve(__dirname, '..', 'build');
const filePath = path.join(outputDir, 'build.json');

if (!fs.existsSync(outputDir)) {
    console.log("Output directory not present");
    process.exit(1);
}

const monitoringVersionsFile = path.resolve(__dirname, '..', 'monitoring_versions.json');

if (!fs.existsSync(monitoringVersionsFile)) {
    console.log("monitoring_versions.json not found");
    process.exit(1);
}

const timestamp = new Date().getTime();

const monitoringVersions = JSON.parse(fs.readFileSync(monitoringVersionsFile, 'utf8'));

const monitoringVersionsIndexMapping = {};
monitoringVersions.forEach((version, index) => {
    if (index === 0) {
        monitoringVersionsIndexMapping[version] = `/search-index.json`;
    } else {
        monitoringVersionsIndexMapping[version] = `/monitoring/${version}/search-index.json`;
    }
});

fs.writeFileSync(filePath, JSON.stringify({
    timestamp: timestamp,
    monitoringIndexes: monitoringVersionsIndexMapping
}), 'utf8');
