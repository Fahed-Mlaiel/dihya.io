/**
 * Immobilier Project Generator
 * @module immobilier/template
 * @description Générateur avancé de projets immobilier (REST, GraphQL, IA, sécurité, i18n, plugins, RGPD)
 * @author Dihya Team
 * @license MIT
 */

'use strict';

const { validateConfig, withI18n, withSecurity, withSEO, withAudit, withPlugins } = require('../../utils');

/**
 * Génère un projet immobilier clé en main.
 * @param {Object} config - Configuration du projet
 * @param {string} config.lang - Langue principale
 * @param {string} config.tenant - Identifiant du tenant
 * @param {string} config.role - Rôle utilisateur
 * @returns {Object} Projet généré
 */
function generateProject(config) {
  validateConfig(config, ['lang', 'tenant', 'role']);
  let project = {
    routes: [
      withSecurity('/api/immobilier/biens', ['GET', 'POST', 'PUT', 'DELETE'], config.role),
      withSecurity('/api/immobilier/locations', ['GET', 'POST'], config.role),
      withSecurity('/api/immobilier/plugins', ['GET', 'POST'], 'admin'),
    ],
    graphql: {
      Bien: {
        fields: ['id', 'adresse', 'type', 'proprietaire'],
        resolvers: {
          query: withSecurity('biens', ['admin', 'user']),
          mutation: withSecurity('bienMutation', ['admin'])
        }
      }
    },
    i18n: withI18n(config.lang),
    seo: withSEO(),
    audit: withAudit(config.tenant),
    plugins: withPlugins('immobilier'),
    rgpd: true
  };
  return project;
}

module.exports = { generateProject };
