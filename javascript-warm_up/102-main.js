#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(-2, function (nb) {
  console.log('New value: ' + nb);
});
