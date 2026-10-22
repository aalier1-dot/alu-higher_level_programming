#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};

Object.keys(dict).forEach((userId) => {
  const occurrences = dict[userId];

  if (!Object.prototype.hasOwnProperty.call(newDict, occurrences)) {
    newDict[occurrences] = [];
  }

  newDict[occurrences].push(userId);
});

console.log(newDict);
