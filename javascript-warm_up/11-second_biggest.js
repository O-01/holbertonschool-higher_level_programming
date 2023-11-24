#!/usr/bin/node
const inputs = process.argv.slice(2);
inputs[1] ? console.log(inputs.sort((x, y) => x - y)[inputs.length - 2]) : console.log(0);
