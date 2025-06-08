// Point d’entrée ultra avancé pour utils
const fs = require('fs');
const path = require('path');

fs.readdirSync(__dirname)
  .filter(f => f.startsWith('sample_utils') && f.endsWith('.js'))
  .forEach(f => {
    module.exports[path.basename(f, '.js')] = require(path.join(__dirname, f));
  });
