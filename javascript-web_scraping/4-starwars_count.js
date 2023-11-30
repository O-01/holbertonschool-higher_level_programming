#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], { timeout: 3000 }, (err, response, body) => {
  if (err) console.error(err);
  else if (response.statusCode === 404) console.log('404 NOT FOUND');
  else if (body) {
    const chars = JSON.parse(body).results.map((film) => film.characters);
    const wedge = chars.reduce((out, char) => out.concat(char.filter((entry) => entry.match(/.\/18\//g))), []);
    console.log(wedge.length);
  }
});
