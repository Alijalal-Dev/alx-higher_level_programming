#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = Object.entries(dict).reduce((outputDict, [key, value]) => {
  outputDict[value] = outputDict[value] ? [...outputDict[value], key] : [key];
  return outputDict;
}, {});

console.log(newDict);
