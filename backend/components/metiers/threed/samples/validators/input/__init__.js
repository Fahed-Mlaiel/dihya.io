// Point d’entrée ultra avancé pour validators input
const fs = require('fs');
const path = require('path');

fs.readdirSync(__dirname)
  .filter(f => f.startsWith('sample_input') && f.endsWith('.js'))
  .forEach(f => {
    module.exports[path.basename(f, '.js')] = require(path.join(__dirname, f));
  });
