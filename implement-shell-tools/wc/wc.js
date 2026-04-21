import { readFile } from "node:fs/promises";

const args = process.argv.slice(2);
const flags = args.filter(arg => arg.startsWith("-"));
const files = args.filter(arg => !arg.startsWith("-"));

const showLines = flags.includes("-l") || flags.length === 0;
const showWords = flags.includes("-w") || flags.length === 0;
const showChars = flags.includes("-c") || flags.length === 0;

let totalLines = 0;
let totalWords = 0;
let totalChars = 0;

function format(num) {
  return num.toString().padStart(8, " ");
}

for (const file of files) {
  try {
    const data = await readFile(file, "utf8");
    const lines = data.split("\n").length - 1;
    const words = data.split(/\s+/).filter(w => w.length > 0).length;
    const chars = Buffer.byteLength(data, "utf8");

    totalLines += lines;
    totalWords += words;
    totalChars += chars;

    let output = "";
    if (showLines) output += format(lines);
    if (showWords) output += format(words);
    if (showChars) output += format(chars);

    console.log(`${output} ${file}`);
  } catch (err) {
    console.error(`wc: ${file}: No such file or directory`);
  }
}

if (files.length > 1) {
    let totalOutput = "";
    if (showLines) totalOutput += format(totalLines);
    if (showWords) totalOutput += format(totalWords);
    if (showChars) totalOutput += format(totalChars);

    console.log(`${totalOutput} total`);
}