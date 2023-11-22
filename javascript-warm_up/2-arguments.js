#!/usr/bin/node
const argvLen = process.argv.length;
if (argvLen === 3) {
  console.log('Argument found');
} else if (argvLen > 3) {
  console.log('Arguments found');
} else {
  console.error('No argument');
}
