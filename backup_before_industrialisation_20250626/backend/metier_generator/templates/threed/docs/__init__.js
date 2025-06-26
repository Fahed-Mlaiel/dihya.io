// Point d'entrée global pour toute la documentation du module threed
const api = require('./api');
const architecture = require('./architecture');
const changelog = require('./changelog');
const faq = require('./faq');
const integration = require('./integration');
const security = require('./security');
const tutorials = require('./tutorials');

module.exports = {
  ...api,
  ...architecture,
  ...changelog,
  ...faq,
  ...integration,
  ...security,
  ...tutorials
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
