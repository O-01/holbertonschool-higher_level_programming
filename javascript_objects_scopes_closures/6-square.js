#!/usr/bin/node
const otherSquare = require('./5-square');
module.exports = class Square extends otherSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let row = 0; row < this.width; row++) console.log((!c ? 'X' : c).repeat(this.width));
  }
};
