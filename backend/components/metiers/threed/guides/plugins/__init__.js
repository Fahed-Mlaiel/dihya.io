// Point d’entrée ultra avancé pour plugins
// Charge dynamiquement tous les guides plugins JS du dossier
const fs = require('fs');
const path = require('path');

fs.readdirSync(__dirname)
  .filter(f => f.endsWith('.guide.js'))
  .forEach(f => {
    module.exports[path.basename(f, '.js')] = require(path.join(__dirname, f));
  });
