import { readdirSync } from "node:fs";

const args = process.argv.slice(2);
const flags = args.filter(arg => arg.startsWith('-'));
const targetDir = args.filter(arg => !arg.startsWith('-'))[0] || ".";

const showAll = flags.includes('-a');
const useVertical = flags.includes('-1');

try {
    let files = readdirSync(targetDir);

    if (showAll) {
        files = [".", "..", ...files];
    } else {
        files = files.filter(f => !f.startsWith('.'));
    }
    files.sort((a, b) => a.localeCompare(b));
    if (useVertical) {
        files.forEach(file => console.log(file));
    } else {
        console.log(files.join(' '));
    }
} catch (err) {
    console.error(`ls: cannot access '${targetDir}': No such file or directory`);
}
