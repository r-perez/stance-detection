/*
 * Webcrawler em JS
 * Fonte: https://gist.github.com/wesleyamaral/b2cf7a45ef66dee5a598cbb8e01b1fe8
 */

const request = require('request');
const cheerio = require('cheerio');
const fs      = require('fs');

// Url a ser visitada
const pageToVisit = 'http://www.suapesquisa.com/geografia/siglas_estados_brasileiros.htm';
console.log('Visiting page ' + pageToVisit);

request(pageToVisit, function (error, response, body) {
  if (error) {
    console.log('Error: ' + error);
  }

  let $ = cheerio.load(body);

  let estados = [];
  let siglas = [];

  // Trata as informaçoes e armazena no arquivo
  $('.body td').each(function () {
    let title   = $(this).text().trim();

    if (title.length > 0) {
      if (title.length > 2) {
        estados.push(title);
        console.log(title);
      } else {
        siglas.push(title);
        console.log(title);
      }
    }

  });

  estados.shift();
  estados.shift();
  const estadoFile = fs.createWriteStream('estados.txt');

  estados.forEach((estado) => {
      estadoFile.write(estado + '\n');
    });
  estadoFile.end();

  const siglasFile = fs.createWriteStream('siglas.txt');
  siglas.forEach((sigla) => {
    siglasFile.write(sigla + '\n');
  });

});