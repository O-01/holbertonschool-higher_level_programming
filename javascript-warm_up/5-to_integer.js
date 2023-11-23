#!/usr/bin/node
const intArg = parseInt(process.argv[2]);
intArg ? console.log(`My number: ${intArg}`) : console.log('Not a number');
