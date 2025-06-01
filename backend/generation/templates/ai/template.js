/**
 * Intelligence Artificielle Project Generator
 * @module intelligence_artificielle/template
 * @description Générateur avancé de projets IA (REST, GraphQL, IA, sécurité, i18n, plugins, RGPD, fallback open source)
 * @author Dihya Team
 * @license MIT
 */

'use strict';

const { validateConfig, withI18n, withSecurity, withSEO, withAudit, withPlugins, withIAFallback } = require('../../utils');

/**
 * Génère un projet IA clé en main.
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
      withSecurity('/api/ia/modeles', ['GET', 'POST', 'PUT', 'DELETE'], config.role),
      withSecurity('/api/ia/datasets', ['GET', 'POST'], config.role),
      withSecurity('/api/ia/plugins', ['GET', 'POST'], 'admin'),
    ],
    graphql: {
      Modele: {
        fields: ['id', 'nom', 'type', 'proprietaire'],
        resolvers: {
          query: withSecurity('modeles', ['admin', 'user']),
          mutation: withSecurity('modeleMutation', ['admin'])
        }
      }
    },
    i18n: withI18n(config.lang),
    seo: withSEO(),
    audit: withAudit(config.tenant),
    plugins: withPlugins('intelligence_artificielle'),
    iaFallback: withIAFallback(['llama', 'mixtral', 'mistral']),
    rgpd: true
  };
  return project;
}

module.exports = { generateProject };
