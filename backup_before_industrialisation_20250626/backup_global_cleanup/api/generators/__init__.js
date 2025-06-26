// Initialisation des générateurs API (Node.js)
const fs = require('fs');
const path = require('path');

const generators = {};
fs.readdirSync(__dirname).forEach(file => {
  if (file.endsWith('.js') && file !== '__init__.js') {
    const name = file.replace('.js', '');
    generators[name] = require('./' + file);
  }
});

module.exports = generators;
