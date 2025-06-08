// index.js – Ultra avancé, clé en main, centralise tous les modules et exports du module Threed
const path = require('path');
const fs = require('fs');

/**
 * Auto-discovery et export dynamique de tous les sous-modules du dossier threed
 * @module threed
 */
fs.readdirSync(__dirname).forEach(dir => {
  const fullPath = path.join(__dirname, dir);
  if (
    fs.statSync(fullPath).isDirectory() &&
    !dir.startsWith('.') &&
    dir !== 'reports' &&
    dir !== 'scripts' &&
    dir !== '__pycache__'
  ) {
    try {
      // Recherche d'un index.js ou d'un module principal dans chaque sous-dossier
      const indexPath = path.join(fullPath, 'index.js');
      if (fs.existsSync(indexPath)) {
        module.exports[dir] = require(indexPath);
      }
    } catch (e) {
      // Ignore si pas de module principal
    }
  }
});
