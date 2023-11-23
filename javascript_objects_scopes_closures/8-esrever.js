#!/usr/bin/node
exports.esrever = function (list) {
  const pushList = [];
  while (list.length) pushList.push(list.pop());
  return pushList;
};
