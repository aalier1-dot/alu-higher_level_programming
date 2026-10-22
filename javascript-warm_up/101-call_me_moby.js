#!/usr/bin/node
function callMeMoby (x, theFunction) {
  let count = 0;

  while (count < x) {
    theFunction();
    count += 1;
  }
}

exports.callMeMoby = callMeMoby;
