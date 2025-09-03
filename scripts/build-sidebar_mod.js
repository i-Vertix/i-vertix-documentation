const path = require("path");
const fs = require("fs");
const jsYaml = require('js-yaml');

const args = require('minimist')(process.argv.slice(2));
console.log(args);
if (!args.versioning) {
    console.error("parameter --versioning missing (e.g. --versioning=22.04)");
    process.exit(1);
}
if (!args.docs) {
    console.error("parameter --docs missing (e.g. --docs=log-management)");
    process.exit(1);
}

const validDocs = ["monitoring", "log-management", "asset-management"];
const docs = args.docs;
let version = args.versioning;

if (!validDocs.includes(docs)) {
    console.error("parameter --docs has an invalid value (available values are: " + validDocs.join(', ') + ")");
    process.exit(1);
    return;
}

if (docs === "monitoring") {
    version = version.toFixed(2);
}

// fs.writeFileSync(path.resolve(`${__dirname}/../alert.js`), fileContent, {enconding: 'utf8'});

const yamlPath = path.resolve(`${__dirname}/../${docs}_versioned_sidebars/${version}-sidebar.yaml`);
let yaml = [];
try {
    yaml = jsYaml.load(fs.readFileSync(yamlPath, 'utf8'), {});
} catch {
    console.error("unable to read file: '" + yamlPath + "'");
    process.exit(1);
    return;
}

const content = [];

const addCategory = (obj, categoryPath, category) => {

    let idx = category.items.findIndex((x) => ("id" in x && x["id"] === "index"))
    if (idx != -1) {
        const idx_obj = category.items[idx]
        category.items.splice(idx, 1)
        obj.push({
            type: "category",
            collapsed: true,
            label: idx_obj.label,
            link: {
                type: "doc",
                id: `${categoryPath}${idx_obj.id}`
            },
            items: []
        });
    }
    else {
        obj.push({
            type: "category",
            collapsed: true,
            label: category.label,
            items: []
        });
    }

    const arr = obj[obj.length - 1].items;
    for (const item of category.items) {
        if (typeof item === "string") {
            addDoc(arr, categoryPath, item);
        } else if (!item.items) {
            addDoc(arr, categoryPath, item);
        } else {
            addCategory(arr, `${categoryPath}${item.id}/`, item);
        }
    }
}

const addDoc = (obj, category, doc) => {
    let d = "";
    let l = undefined;
    if (typeof doc === "string") {
        d = doc;
    } else {
        d = doc.id;
        l = doc.label;
    }
    obj.push({
        type: "doc",
        id: `${category}${d}`,
        label: l
    });
}

for (const item of yaml.sidebar) {
    if (typeof item === "string") {
        addDoc(content, '', item);
    } else if (!item.items) {
        addDoc(content, '', item);
    } else {
        addCategory(content, `${item.id}/`, item);
    }
}


const sidebar = JSON.stringify({
    [`docs`]: content
});

const outputPath = path.resolve(`${__dirname}/../${docs}_versioned_sidebars/version-${version}-sidebars.json`);
console.log(sidebar);
fs.writeFileSync(outputPath, sidebar, {encoding: 'utf8'});
process.exit(0);