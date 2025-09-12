const path = require("path");
const fs = require("fs");
const jsYaml = require('js-yaml');

const args = require('minimist')(process.argv.slice(2));
console.log("Args:", args);

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

let content = [];

const addCategory = (obj, categoryPath, category) => {

    obj.push({
        type: "category",
        collapsed: true,
        label: category.label,
        items: []
    });

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


const setCategoryIndex = (items) => {

    let res = []

    for (const item of items.filter(
        (x) => !("id" in x && x.id.endsWith("index"))
    )) {

        if (item.type === "category") {

            const category = item

            let index_elem = item.items.find(
                (x) => ("id" in x && x.id.endsWith("index"))
            )
            if (index_elem) {
                category.link = {
                    type: "doc",
                    id: index_elem.id
                }
            }
            category.items = setCategoryIndex(item.items)
            res.push(category)
        }
        else if (item.type === "doc") {
            res.push(item)
        }
        else {
            console.log("ERROR!")
            //should not happen!
        }
    }
    return res
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

// restricting index categories processing to asset-management
// i.e. make all sidebar categories become a link pointing
// to the index page
if (args.docs === "asset-management") {
    //we need to keep the - otherwise filtered - first element
    content = [content[0]].concat(setCategoryIndex(content.slice(1)))
}

const sidebar = JSON.stringify({
    [`docs`]: content
},
    null,
    2
);

const outputPath = path.resolve(`${__dirname}/../${docs}_versioned_sidebars/version-${version}-sidebars.json`);
//console.log(sidebar);
fs.writeFileSync(outputPath, sidebar, { encoding: 'utf8' });
process.exit(0);