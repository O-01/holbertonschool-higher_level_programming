#!/usr/bin/node
const fs = require('fs');
const files = process.argv.slice(2);
fs.writeFileSync(files[2], fs.readFileSync(files[0]) + fs.readFileSync(files[1]));
