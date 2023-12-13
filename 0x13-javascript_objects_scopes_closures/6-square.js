#!/usr/bin/node

const baseSquare = require('./5-square');

class Square extends baseSquare {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.width; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += c;
        }
        console.log(row);
      }
    } else {
      for (let i = 0; i < this.width; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += 'X';
        }
        console.log(row);
      }
    }
  }
}

module.exports = Square;
