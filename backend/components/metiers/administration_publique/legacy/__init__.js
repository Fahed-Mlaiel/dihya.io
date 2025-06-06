// __init__.js - Initialisation du dossier legacy pour le module Threed
const fs = require('fs');
const path = require('path');

fs.readdirSync(__dirname).forEach(file => {
  if (file.endsWith('.js') && file !== '__init__.js') {
    require(path.join(__dirname, file));
  }
});
