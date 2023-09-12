#!/usr/bin/node

class Rectangle {
    constructor (w, h) {
// Check if both w and h are positive numbers
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  }
  
  module.exports = Rectangle;
  