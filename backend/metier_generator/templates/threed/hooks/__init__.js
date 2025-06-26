// Point d'entrée global pour tous les hooks du module threed
const asset = require('./asset');
const audit = require('./audit');
const customEvent = require('./custom_event');
const lifecycle = require('./lifecycle');
const notification = require('./notification');

module.exports = {
  ...asset,
  ...audit,
  ...customEvent,
  ...lifecycle,
  ...notification
};

// Initialisation avancée du module JS
const fs = require('fs');
const path = require('path');
function loadModules(dir) {
  fs.readdirSync(dir).forEach(file => {
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      loadModules(fullPath);
    } else if (file.endsWith('.js') && file !== '__init__.js') {
      require(fullPath);
    }
  });
}
loadModules(__dirname);
