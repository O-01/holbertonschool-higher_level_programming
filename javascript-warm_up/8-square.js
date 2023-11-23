#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (size) for (let row = 0; row < size; row++) console.log('X'.repeat(size));
else console.log('Missing size');
