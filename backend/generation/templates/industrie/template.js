/**
 * Industrie Project Generator
 * @module industrie/template
 * @description Générateur avancé de projets industrie (REST, GraphQL, IA, sécurité, i18n, plugins, RGPD)
 * @author Dihya Team
 * @license MIT
 */

'use strict';

const { validateConfig, withI18n, withSecurity, withSEO, withAudit, withPlugins } = require('../../utils');

/**
 * Génère un projet industrie clé en main.
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
      withSecurity('/api/industrie/equipements', ['GET', 'POST', 'PUT', 'DELETE'], config.role),
      withSecurity('/api/industrie/maintenance', ['GET', 'POST'], config.role),
      withSecurity('/api/industrie/plugins', ['GET', 'POST'], 'admin'),
    ],
    graphql: {
      Equipement: {
        fields: ['id', 'nom', 'type', 'proprietaire'],
        resolvers: {
          query: withSecurity('equipements', ['admin', 'user']),
          mutation: withSecurity('equipementMutation', ['admin'])
        }
      }
    },
    i18n: withI18n(config.lang),
    seo: withSEO(),
    audit: withAudit(config.tenant),
    plugins: withPlugins('industrie'),
    rgpd: true
  };
  return project;
}

module.exports = { generateProject };
