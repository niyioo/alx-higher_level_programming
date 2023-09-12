#!/usr/bin/node

class Rectangle {
    constructor(w, h) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      } else {
        // Create an empty object if w or h is not a positive integer
        return {};
      }
    }
  
    print() {
      if (this.width && this.height) {
        for (let i = 0; i < this.height; i++) {
          console.log('X'.repeat(this.width));
        }
      }
    }
  
    rotate() {
      // Exchange the width and height
      if (this.width && this.height) {
        const temp = this.width;
        this.width = this.height;
        this.height = temp;
      }
    }
  
    double() {
      // Double the width and height
      if (this.width && this.height) {
        this.width *= 2;
        this.height *= 2;
      }
    }
  }
  
  module.exports = Rectangle;
  