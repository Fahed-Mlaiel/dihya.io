// index.js – Point d'entrée racine pour tous les tests JS du module api/samples
const fs = require('fs');
const path = require('path');

function requireAllTests(dir) {
  fs.readdirSync(dir).forEach(file => {
    const filePath = path.join(dir, file);
    if (fs.statSync(filePath).isDirectory()) {
      requireAllTests(filePath);
    } else if (file.endsWith('.test.js')) {
      require(filePath);
    }
  });
}

requireAllTests(__dirname);

module.exports = { requireAllTests };
