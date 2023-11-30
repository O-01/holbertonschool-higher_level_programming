#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], { timeout: 3000 }, (err, response, body) => {
  if (err) console.error(err);
  else if (response.statusCode === 404) console.log('404 NOT FOUND');
  else if (body) {
    const completed = JSON.parse(body).filter((entry) => entry.completed === true);
    const totalCompletedById = completed.reduce((out, task) => {
      return ((out[task.userId] = completed.filter((view) => view.userId === task.userId).length), out);
    }, {});
    console.log(totalCompletedById);
  }
});
