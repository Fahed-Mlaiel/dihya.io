// __init__.js – Initialisation avancée du dossier samples (connectors)

/**
 * Ce fichier permet l’import dynamique, l’auto-discovery et l’extension future des exemples de connecteurs Threed.
 * Prêt pour l’industrialisation, l’audit, la RGPD, l’accessibilité, la documentation et l’intégration CI/CD.
 * Peut être enrichi pour charger dynamiquement tous les exemples JS présents dans ce dossier.
 */

const fs = require('fs');
const path = require('path');

const samples = {};

fs.readdirSync(__dirname).forEach(file => {
  if (file.startsWith('example_') && file.endsWith('.js')) {
    const mod = require(path.join(__dirname, file));
    samples[file.replace('.js', '')] = mod;
  }
});

// Import dynamique des sous-dossiers d'exemples (adapters, exporters, importers, plugins)
['adapters', 'exporters', 'importers', 'plugins'].forEach(subdir => {
  try {
    samples[subdir] = require(path.join(__dirname, subdir));
  } catch (e) {}
});

module.exports = samples;
