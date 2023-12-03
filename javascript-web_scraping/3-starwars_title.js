#!/usr/bin/node
const request = require('request');
request
  .get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, response, body) => {
    if (err) console.error(err);
    else if (response.statusCode === 404) console.log('404 NOT FOUND');
    else if (body) console.log(JSON.parse(body).title);
  });

// Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
// - The first argument is the movie ID
// - You must use the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
// - You must use the module request
// EXAMPLE: ./3-starwars_title.js 1
