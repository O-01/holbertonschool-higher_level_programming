#!/usr/bin/node
const dict = require('./101-data').dict;
const dictById = Object.entries(dict).reduce((dump, [k, v]) => {
  return ((dump[v] || (dump[v] = [])).push(k), dump);
}, {});
console.log(dictById);
