// Initialisation des scripts DevOps (Node.js)
const fs = require('fs');
const path = require('path');

const scripts = {};
fs.readdirSync(__dirname).forEach(file => {
  if (file.endsWith('.js') && file !== '__init__.js') {
    const name = file.replace('.js', '');
    scripts[name] = require('./' + file);
  }
});

module.exports = scripts;
