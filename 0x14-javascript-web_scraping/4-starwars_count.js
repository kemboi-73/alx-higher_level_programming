#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let num = 0;
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.log(`status code: ${response.statusCode}`);
    return;
  }
  const res = JSON.parse(body);
  const movies = res.results;
  for (let i = 0; i < movies.length; ++i) {
    const characters = movies[i].characters;
    for (let j = 0; j < characters.length; ++j) {
      const character = characters[j];
      const characterId = character.split('/')['5'];
      if (characterId === '18') {
        num += 1;
      }
    }
  }
  console.log(num);
});
