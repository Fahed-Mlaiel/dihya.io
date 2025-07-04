// Initialisation avancée du module helpers (auto-discovery, export dynamique, documentation)
const fs = require('fs');
const path = require('path');

/**
 * Auto-discovery et export dynamique de tous les modules JS du dossier
 * @module helpers
 */
fs.readdirSync(__dirname).forEach(file => {
  if (file.endsWith('.js') && !file.startsWith('__init__')) {
    const mod = require(path.join(__dirname, file));
    Object.assign(module.exports, mod);
  }
});
