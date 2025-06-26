// Initialisation racine des blueprints (Node.js)
// Exporte dynamiquement tous les sous-dossiers métiers avec auto-détection
const fs = require('fs');
const path = require('path');

const blueprints = {};
fs.readdirSync(__dirname).forEach(dir => {
  if (fs.existsSync(path.join(__dirname, dir, '__init__.js'))) {
    blueprints[dir] = require(`./${dir}`);
  }
});

module.exports = blueprints;

// Documentation intégrée
/**
 * Utilisation :
 * const { api, devops, webApp, mobileApp } = require('./blueprints');
 * const app = api.backendApi({ metier: 'Inventaire' });
 */
