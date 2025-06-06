// Initialisation du module de tests views/samples
// Découverte automatique, helpers, CI/CD
const fs = require('fs');
module.exports.discover = () => {
  return fs.readdirSync(__dirname).filter(f => f.endsWith('.test.js'));
};
