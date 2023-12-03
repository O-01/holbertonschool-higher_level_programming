#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], { timeout: 3000 }, (err, response, body) => {
  if (err) console.error(err);
  else if (response.statusCode === 404) console.log('404 NOT FOUND');
  else {
    const fs = require('fs');
    fs.writeFile(process.argv[3], body, 'utf8', (err) => { if (err) throw err; });
  }
});

// Write a script that gets the contents of a webpage and stores it in a file.
// - The first argument is the URL to request
// - The second argument the file path to store the body response
// - The file must be UTF-8 encoded
// - You must use the module request
// EXAMPLE: ./5-request_store.js http://loripsum.net/api loripsum
