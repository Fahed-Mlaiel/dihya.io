// __init__.js - Initialisation du dossier plugins pour le module threed

const fs = require('fs');
const path = require('path');

fs.readdirSync(__dirname).forEach(file => {
  if (file.endsWith('.js') && file !== '__init__.js') {
    require(path.join(__dirname, file));
  }
});

module.exports = {
  ...require('./core'),
  ...require('./helpers'),
  ...require('./samples'),
};
