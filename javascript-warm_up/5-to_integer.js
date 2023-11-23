#!/usr/bin/node
const intArg = parseInt(process.argv[2]);
if (intArg) console.log(`My number: ${intArg}`);
else console.log('Not a number');
