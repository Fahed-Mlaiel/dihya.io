// Initialisation du module de tests services/core
// Découverte automatique, helpers, CI/CD
const requireDirectory = require('require-directory');
const fs = require('fs');

module.exports = requireDirectory(module, __dirname);

module.exports.discover = () => {
  return fs.readdirSync(__dirname).filter(f => f.endsWith('.test.js'));
};
