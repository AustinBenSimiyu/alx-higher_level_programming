#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movies = JSON.parse(body).results;
    const charArray = movies.map(movie => movie.characters)
      .filter(x => x.includes('https://swapi-api.hbtn.io/api/people/18/'));
    console.log(charArray.length);
  }
});
