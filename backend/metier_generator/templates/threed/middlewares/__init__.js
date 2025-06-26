// Point d'entrée global pour tous les middlewares du module threed
const context = require('./context');
const logger = require('./logger');
const security = require('./security');
const validation = require('./validation');

module.exports = {
  ...context,
  ...logger,
  ...security,
  ...validation
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
