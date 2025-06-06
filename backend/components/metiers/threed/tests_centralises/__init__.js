// Initialisation du module de tests centralisés threed
// Découverte automatique, helpers, CI/CD
const fs = require('fs');
const path = require('path');
module.exports.discover = () => {
  const walk = dir => fs.readdirSync(dir).flatMap(f => {
    const p = path.join(dir, f);
    return fs.statSync(p).isDirectory() ? walk(p) : p;
  });
  return walk(__dirname).filter(f => f.endsWith('.test.js'));
};
