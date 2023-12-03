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

// Write a script that prints the number of movies where the character “Wedge Antilles” is present.
// - The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
// - Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
// - You must use the module request
// EXAMPLE: ./4-starwars_count.js https://swapi-api.hbtn.io/api/films
