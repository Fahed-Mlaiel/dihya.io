// service.js - Service principal Dihya Frontend
/**
 * @file Service principal pour la gestion des projets IA, VR, AR, multitenancy, sécurité, i18n, SEO, plugins, RGPD, auditabilité.
 * @author Dihya
 * @version 1.0
 */

const { initI18n, getUserRole, secureRoute } = require('../utils');
const { addPlugin, runPlugin } = require('../plugins');
const { monitorPerformance } = require('../monitoring');
const { generateSitemap } = require('../seo');

/**
 * Initialise le service principal Dihya
 * @param {Object} config - Configuration du service
 * @returns {Object} - Instance du service
 */
function initService(config) {
  initI18n(config.langs);
  monitorPerformance();
  return {
    addPlugin,
    runPlugin,
    generateSitemap,
    secureRoute,
    getUserRole,
  };
}

module.exports = { initService };
