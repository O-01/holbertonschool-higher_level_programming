#!/usr/bin/node
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf8', (err) => {
  if (err) console.error(err);
});

// Write a script that writes a string to a file.
// - The first argument is the file path
// - The second argument is the string to write
// - The content of the file must be written in utf-8
// - If an error occurred during while writing, print the error object
// EXAMPLE: ./1-writeme.js <fileName> <string>
