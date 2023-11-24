#!/usr/bin/node
const inputs = process.argv.slice(2).sort((x, y) => x - y);
inputs[1] ? console.log(inputs[inputs.length - 2]) : console.log(0);
