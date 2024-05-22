#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  try {
    fs.writeFile(filePath, body, 'utf8', (err, result) => {
      if (err) console.log(err);
    });
  } catch (err) {
    console.log(err);
  }
});
