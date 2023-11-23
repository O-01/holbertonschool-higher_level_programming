#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  if (x > 0) for (let occur = 0; occur !== x; occur++) theFunction();
  else return;
};
