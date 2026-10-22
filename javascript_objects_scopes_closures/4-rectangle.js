#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!Number.isInteger(w) || w <= 0 || !Number.isInteger(h) || h <= 0) {
      return;
    }

    this.width = w;
    this.height = h;
  }

  print () {
    for (let row = 0; row < this.height; row += 1) {
      let line = '';
      for (let column = 0; column < this.width; column += 1) {
        line += 'X';
      }
      console.log(line);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
