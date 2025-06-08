// index.js – Point d'entrée ultra avancé, clé en main, pour le dossier connectors (racine)
/**
 * Centralise l'import/export dynamique de tous les sous-dossiers (adapters, exporters, importers, plugins, samples).
 * Prêt pour l’industrialisation, l’audit, la RGPD, l’accessibilité, la documentation, la CI/CD, la multi-langue, l’extension et l’auto-discovery.
 */
const path = require('path');
const fs = require('fs');
const modules = {};
['adapters', 'exporters', 'importers', 'plugins', 'samples'].forEach(subdir => {
  try {
    modules[subdir] = require(path.join(__dirname, subdir));
  } catch (e) {}
});
// Import dynamique des exemples à la racine
fs.readdirSync(__dirname).forEach(file => {
  if (file.startsWith('example_') && file.endsWith('.js')) {
    modules[file.replace('.js', '')] = require(path.join(__dirname, file));
  }
});
module.exports = modules;
