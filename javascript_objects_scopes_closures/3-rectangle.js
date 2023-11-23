#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w && h) > 0) [this.width, this.height] = [w, h];
  }

  print () {
    for (let row = 0; row < this.height; row++) console.log('X'.repeat(this.width));
  }
};
