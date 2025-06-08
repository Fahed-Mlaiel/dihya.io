// index.js – Ultra avancé, clé en main, centralise tous les modules et exports
const path = require('path');
const fs = require('fs');

/**
 * Auto-discovery et export dynamique de tous les sous-modules du dossier utils
 * @module utils
 */
fs.readdirSync(__dirname).forEach(dir => {
  const fullPath = path.join(__dirname, dir);
  if (fs.statSync(fullPath).isDirectory() && !dir.startsWith('.')) {
    try {
      const mod = require(path.join(fullPath, 'index.js'));
      module.exports[dir] = mod;
    } catch (e) {
      // Ignore si pas de index.js
    }
  }
});
