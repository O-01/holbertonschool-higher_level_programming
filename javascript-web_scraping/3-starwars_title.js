#!/usr/bin/node
const request = require('request');
request
  .get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, response, body) => {
    if (err) console.error(err);
    else if (response.statusCode === 404) console.log('404 NOT FOUND');
    else if (body) console.log(JSON.parse(body).title);
  });
