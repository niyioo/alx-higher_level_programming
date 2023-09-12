#!/usr/bin/node

// Import the Square class from 5-square.js
const BaseSquare = require ('./5-square');

class Square extends BaseSquare {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }

    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
