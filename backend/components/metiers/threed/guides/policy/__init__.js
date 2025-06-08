// Point d’entrée ultra avancé pour policy
// Charge dynamiquement tous les guides policy JS du dossier
const fs = require('fs');
const path = require('path');

fs.readdirSync(__dirname)
  .filter(f => f.endsWith('.guide.js'))
  .forEach(f => {
    module.exports[path.basename(f, '.js')] = require(path.join(__dirname, f));
  });
