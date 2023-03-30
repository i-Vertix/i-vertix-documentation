const path = require("path");
const fs = require("fs");
const readline = require('readline');

function waitForUserInput(question) {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    });

    return new Promise(resolve => rl.question(question, ans => {
        rl.close();
        resolve(ans);
    }))
}

const header = () => {
    console.log("Generate i-Vertix Documentation Alerts\n");
}

const getTitle = async () => {
    console.clear();
    header();
    const val = await waitForUserInput("\x1b[42mTitle*:\x1b[0m ");
    if (val.trim() === "") {
        return await getTitle();
    }
    return val;
}

const getImage = async () => {
    // header();
    const val = await waitForUserInput("\x1b[42mImage Path (optional):\x1b[0m ");
    if (val.trim() === "") {
        return undefined;
    }
    return val;
}

const getSize = async () => {
    const val = await waitForUserInput("\x1b[42mSize (small|medium):\x1b[0m ");
    if (val !== "small") {
        return "medium";
    }
    return val;
}

const _getDescription = async (arr) => {
    const val = await waitForUserInput("");
    if (val.trim() === "") {
        return arr;
    }
    arr.push(val);
    return await _getDescription(arr);
}

const getDescription = async () => {
    // header();
    console.log("\x1b[42mDescription (optional):\x1b[0m");
    return await _getDescription([]);
}

const getLink = async () => {
    // header();
    const url = await waitForUserInput("\x1b[42mLink Url (optional):\x1b[0m ");
    if (url.trim() === "") {
        return undefined;
    }
    const label = await waitForUserInput("\x1b[42mLink Text:\x1b[0m ");
    if (label.trim() === "") {
        return await getLink();
    }
    return {to: url, label: label};
}

const run = async () => {
    const title = await getTitle();
    const description = await getDescription();
    const size = await getSize();
    const image = await getImage();
    const link = await getLink();
    const timestamp = new Date().getTime();
    let fileContent = `const alert = {
    timestamp: ${timestamp},
    title: "${title}",
    description: [
        ${description.map(v => `"${v}"`).join(',\n\t\t')}
    ],
    size: "${size}",
    image: ${image ? `"${image}"` : `undefined`},
    link: ${link ? `{
        label: "${link.label}",
        to: "${link.to}"
    }` : `undefined`}
};

module.exports = alert;`;
    fs.writeFileSync(path.resolve(`${__dirname}/../alert.js`), fileContent, {enconding: 'utf8'});
    console.log("\n", fileContent);
}

run();