#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let occur = 0; occur !== x; occur++) theFunction();
};
