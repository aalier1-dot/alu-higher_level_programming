#!/usr/bin/node
const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (c) {
    const character = c === undefined ? 'X' : c;

    for (let row = 0; row < this.height; row += 1) {
      let line = '';
      for (let column = 0; column < this.width; column += 1) {
        line += character;
      }
      console.log(line);
    }
  }
}

module.exports = Square;
