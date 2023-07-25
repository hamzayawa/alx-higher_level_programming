#!/usr/bin/node
const request = require('request');
const endPoint = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request({ url: endPoint, methods: 'GET' }, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(body && JSON.parse(body).title);
  }
});
