#!/usr/bin/node
const argvInputs = process.argv.slice(2);
if (!argvInputs[1]) console.log(0);
else {
  const argSort = argvInputs.sort(function (x, y) { return x - y; });
  console.log(argSort[argSort.length - 2]);
}
