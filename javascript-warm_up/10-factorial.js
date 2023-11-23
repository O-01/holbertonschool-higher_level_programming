#!/usr/bin/node
function factorial (input) {
  if (input < 0) return -1;
  else return input > 1 ? input * factorial(input - 1) : 1;
}
const input = parseInt(process.argv[2]);
console.log(factorial(input));
