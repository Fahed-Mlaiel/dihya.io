// index.js – Ultra avancé, clé en main, centralise tous les modules et exports du module Threed
const path = require('path');
const fs = require('fs');

/**
 * Auto-discovery et export dynamique de tous les sous-modules du dossier threed
 * @module threed
 */
fs.readdirSync(__dirname).forEach(dir => {
  const fullPath = path.join(__dirname, dir);
  if (fs.statSync(fullPath).isDirectory() && !dir.startsWith('.')) {
    try {
      const mod = require(path.join(fullPath, '__init__.js'));
      module.exports[dir] = mod;
    } catch (e) {
      // Ignore si pas de __init__.js
    }
  }
});
