#!/usr/bin/node
const intArg = parseInt(process.argv[2]);
if (intArg) {
  for (let row = 0; row < intArg; row++) {
    for (let col = 0; col < intArg; col++) process.stdout.write('X');
    console.log();
  }
} else console.log('Missing size');
