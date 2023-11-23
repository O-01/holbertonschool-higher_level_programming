#!/usr/bin/node
exports.esrever = function (list) {
  return list.map((elem, idx) => { return list[list.length - idx - 1]; });
};
