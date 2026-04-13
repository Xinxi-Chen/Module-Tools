import { readFile } from "node:fs/promises";

const args = process.argv.slice(2);
const flags = args.filter(arg => arg.startsWith('-'));
const files = args.filter(arg => !arg.startsWith('-'));

const showAll = flags.includes('-n');
const showNonEmpty = flags.includes('-b');

let lineCount = 1;

for (const file of files) {
    try {
        const data = await readFile(file, 'utf8');
        const lines = data.split(/\r?\n/);

        for (const line of lines) {
            if (showNonEmpty && line.trim() === "") {
                console.log("");
            } else if (showAll || (showNonEmpty && line.trim() !== "")) {
                const num = lineCount.toString().padStart(6, ' ');
                console.log(`${num}\t${line}`);
                lineCount++;
            } else {
                console.log(line);
            }
        }
    } catch (err) {
        console.error(`cat: ${file}: No such file`);
    }
}