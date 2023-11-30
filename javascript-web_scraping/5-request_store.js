#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], { timeout: 3000 }, (err, response, body) => {
  if (err) console.error(err);
  else if (response.statusCode === 404) console.log('404 NOT FOUND');
  else {
    const fs = require('fs');
    fs.writeFile(process.argv[3], body, 'utf8', (err) => { if (err) throw err });
  }
});
