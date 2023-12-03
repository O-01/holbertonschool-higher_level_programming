#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], { timeout: 1000 }, (err, response) => {
  if (err) console.error(err);
  else if (response) console.log(`code: ${response.statusCode}`);
});

// Write a script that display the status code of a GET request.
// - The first argument is the URL to request (GET)
// - The status code must be printed like this: code: <status code>
// - You must use the module request
// EXAMPLE: ./2-statuscode.js <url>
