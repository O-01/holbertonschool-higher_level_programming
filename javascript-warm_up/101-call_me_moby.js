#!/usr/bin/node
exports.callMeMoby = (x, theFunction) => {
  if (x > 0) while (x--) theFunction();
};
