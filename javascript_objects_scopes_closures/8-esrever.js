#!/usr/bin/node
exports.esrever = function (list) {
  return list.map((elem, idx) => list[list.length - idx - 1]);
};
