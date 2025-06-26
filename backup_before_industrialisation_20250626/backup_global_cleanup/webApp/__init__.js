// Initialisation des blueprints webApp (Node.js)
const { createWebApp, WebHook } = require('./webapp');

module.exports = {
  createWebApp,
  WebHook
};

// Documentation intégrée
/**
 * Utilisation :
 * const { createWebApp, WebHook } = require('./webApp');
 * const app = createWebApp(...);
 */
