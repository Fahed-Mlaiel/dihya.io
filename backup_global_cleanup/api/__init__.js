// Initialisation avancée des blueprints API (Node.js)
// Exports centralisés, auto-discovery, extension dynamique, documentation intégrée
const fs = require('fs');
const path = require('path');
const apiModules = {};
fs.readdirSync(__dirname + '/routes').forEach(f => {
  if (f.endsWith('.js')) {
    const name = f.replace('.js', '');
    apiModules[name] = require('./routes/' + f);
  }
});
const { backendApi } = require('./generators/backendApi');
module.exports = {
  ...apiModules,
  backendApi
};
/**
 * Exemple d'utilisation :
 * const { backendApi, asset_routes } = require('./api');
 * const app = backendApi({ metier: 'Inventaire' });
 */
