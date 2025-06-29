// Initialisation des routes API (Node.js)
const fs = require('fs');
const path = require('path');

const routes = {};
fs.readdirSync(__dirname).forEach(file => {
  if (file.endsWith('.js') && file !== '__init__.js') {
    const name = file.replace('.js', '');
    routes[name] = require('./' + file);
  }
});

module.exports = routes;
