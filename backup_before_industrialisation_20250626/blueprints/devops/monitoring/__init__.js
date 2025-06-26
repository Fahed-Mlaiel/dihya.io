// Initialisation du monitoring DevOps (Node.js)
const fs = require('fs');
const path = require('path');

const monitoring = {};
fs.readdirSync(__dirname).forEach(file => {
  if (file.endsWith('.js') && file !== '__init__.js') {
    const name = file.replace('.js', '');
    monitoring[name] = require('./' + file);
  }
});

module.exports = monitoring;
