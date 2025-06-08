// Point d’entrée ultra avancé pour rgpd
// Charge dynamiquement tous les guides RGPD JS du dossier
const fs = require('fs');
const path = require('path');

fs.readdirSync(__dirname)
  .filter(f => f.endsWith('.guide.js'))
  .forEach(f => {
    module.exports[path.basename(f, '.js')] = require(path.join(__dirname, f));
  });
