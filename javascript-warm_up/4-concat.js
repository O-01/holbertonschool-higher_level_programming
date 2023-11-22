#!/usr/bin/node
const argVector = process.argv;
if (argVector.length === 2) {
  console.log('No argument');
} else {
  console.log(`${argVector[2]} is ${argVector[3]}`);
}
