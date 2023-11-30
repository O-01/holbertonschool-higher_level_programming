#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], { timeout: 3000 }, (err, response, body) => {
  if (err) console.error(err);
  else if (response.statusCode === 404) console.log('404 NOT FOUND');
  else if (body) {
    const characters = JSON.parse(body).results.map((film) => film.characters)
    const wedges = characters.reduce((out, char) => out.concat(char.filter((entry) => entry.match(/.\/18\//g))), [])
    console.log(wedges.length);
  }
});

// const results = JSON.parse(body).results
// results.forEach((film) => {
//   film.characters.forEach((character) => {
//     if (character.match(/.\/18\//g)) console.log('Found');
//   })
// });
// console.log(results);
