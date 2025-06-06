// __init__.js - Initialisation du dossier views pour le module threed

const fs = require('fs');
const path = require('path');

fs.readdirSync(__dirname).forEach(file => {
  if (file.endsWith('.js') && file !== '__init__.js') {
    require(path.join(__dirname, file));
  }
});

module.exports = require('./router');
