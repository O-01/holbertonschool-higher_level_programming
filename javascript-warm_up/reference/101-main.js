#!/usr/bin/node
const callMeMoby = require('../101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
callMeMoby(-5, function () {
  console.log('C is fun');
});
callMeMoby(6, function () {
  console.log('Check it out');
});
callMeMoby(1, function () {
  console.log('Gotcha');
});
const x = 3
callMeMoby(x, function () {
  console.log('What');
});
