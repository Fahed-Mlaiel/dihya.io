// Point d’entrée ultra avancé pour audit
const fs = require('fs');
const path = require('path');

// Exporte dynamiquement tous les scripts d’audit du dossier
fs.readdirSync(__dirname)
  .filter(f => f.startsWith('sample_audit') && f.endsWith('.js'))
  .forEach(f => {
    module.exports[path.basename(f, '.js')] = require(path.join(__dirname, f));
  });
