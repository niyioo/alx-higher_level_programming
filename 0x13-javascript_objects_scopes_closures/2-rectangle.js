#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if w or h is not positive integers
      // or if either w or h is equal to 0
      Object.create(null);
    }
  }
}

module.exports = Rectangle;
