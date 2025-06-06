// Initialisation du module de tests templates/core
// Découverte automatique, helpers, CI/CD
const fs = require('fs');
module.exports.discover = () => {
  return fs.readdirSync(__dirname).filter(f => f.endsWith('.test.js'));
};
