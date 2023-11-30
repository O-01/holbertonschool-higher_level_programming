#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], (err, response) => {
  if (err) console.error(`error: ${err}`);
  else if (response) console.log(`code: ${response.statusCode}`);
});
