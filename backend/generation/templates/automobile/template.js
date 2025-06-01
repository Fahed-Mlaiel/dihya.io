/**
 * Automobile Project Generator
 * @module automobile/template
 * @description Générateur avancé de projets automobile (REST, GraphQL, IA, sécurité, i18n, plugins, RGPD)
 * @author Dihya Team
 * @license MIT
 */

'use strict';

const { validateConfig, withI18n, withSecurity, withSEO, withAudit, withPlugins } = require('../../utils');

/**
 * Génère un projet automobile clé en main.
 * @param {Object} config - Configuration du projet
 * @param {string} config.lang - Langue principale (fr, en, ar, de, ...)
 * @param {string} config.tenant - Identifiant du tenant
 * @param {string} config.role - Rôle utilisateur (admin, user, invité)
 * @returns {Object} Projet généré
 */
function generateProject(config) {
  validateConfig(config, ['lang', 'tenant', 'role']);
  let project = {
    routes: [
      withSecurity('/api/automobile/vehicules', ['GET', 'POST', 'PUT', 'DELETE'], config.role),
      withSecurity('/api/automobile/diagnostics', ['GET', 'POST'], config.role),
      withSecurity('/api/automobile/plugins', ['GET', 'POST'], 'admin'),
    ],
    graphql: {
      Vehicule: {
        fields: ['id', 'marque', 'modele', 'annee', 'proprietaire'],
        resolvers: {
          query: withSecurity('vehicules', ['admin', 'user']),
          mutation: withSecurity('vehiculeMutation', ['admin'])
        }
      }
    },
    i18n: withI18n(config.lang),
    seo: withSEO(),
    audit: withAudit(config.tenant),
    plugins: withPlugins('automobile'),
    rgpd: true
  };
  return project;
}

module.exports = { generateProject };
