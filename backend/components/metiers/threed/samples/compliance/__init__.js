// Point d’entrée ultra avancé pour compliance
const fs = require('fs');
const path = require('path');

fs.readdirSync(__dirname)
  .filter(f => f.startsWith('sample_compliance') && f.endsWith('.js'))
  .forEach(f => {
    module.exports[path.basename(f, '.js')] = require(path.join(__dirname, f));
  });
