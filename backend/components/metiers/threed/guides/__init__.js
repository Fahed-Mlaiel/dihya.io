/* global __dirname */
// __init__.js - Initialisation du dossier guides pour le module Threed

// Ce fichier peut servir à charger automatiquement tous les guides JS du dossier.
const fs = require('fs');
const path = require('path');

fs.readdirSync(__dirname).forEach(file => {
  if (file.endsWith('.js') && file !== '__init__.js') {
    require(path.join(__dirname, file));
  }
});

// Point d’entrée guides ultra avancé, clé en main
module.exports = {
  ...require('./core/guide_plugins'),
  ...require('./helpers/helpers_plugins'),
  ...require('./fallback/fallback_plugins'),
  ...require('./core/guide_services'),
  ...require('./helpers/helpers_services'),
  ...require('./fallback/fallback_services'),
  ...require('./core/guide_accessibility'),
  ...require('./helpers/helpers_accessibility'),
  ...require('./fallback/fallback_accessibility'),
  // ...autres guides à ajouter ici
};
