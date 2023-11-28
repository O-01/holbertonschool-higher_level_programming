#!/usr/bin/node
const inputs = process.argv.slice(2);
inputs[1] ? console.log(inputs.sort((x, y) => y - x)[1]) : console.log(0);
