#!/usr/bin/node
function factorial (input) {
  return input < 0 ? -1 : input > 1 ? input * factorial(input - 1) : 1;
}
console.log(factorial(parseInt(process.argv[2])));
