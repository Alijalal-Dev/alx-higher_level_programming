#!/usr/bin/node
const bassSquare = require('./5-square');

module.exports = class Square extends bassSquare {
  charPrint (c) {
    if (typeof c === 'undefined') c = 'X';
    for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
  }
};
