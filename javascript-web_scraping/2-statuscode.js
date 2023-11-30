#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], { timeout: 1000 }, (err, response) => {
  if (err) console.error(err);
  else if (response) console.log(`code: ${response.statusCode}`);
});
