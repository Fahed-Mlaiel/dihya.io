/**
 * IT/DevOps Project Generator
 * @module it_devops/template
 * @description Générateur avancé de projets IT/DevOps (REST, GraphQL, IA, sécurité, i18n, plugins, RGPD)
 * @author Dihya Team
 * @license MIT
 */

'use strict';

const { validateConfig, withI18n, withSecurity, withSEO, withAudit, withPlugins } = require('../../utils');

/**
 * Génère un projet IT/DevOps clé en main.
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
      withSecurity('/api/it_devops/pipelines', ['GET', 'POST', 'PUT', 'DELETE'], config.role),
      withSecurity('/api/it_devops/jobs', ['GET', 'POST'], config.role),
      withSecurity('/api/it_devops/plugins', ['GET', 'POST'], 'admin'),
    ],
    graphql: {
      Pipeline: {
        fields: ['id', 'nom', 'status', 'proprietaire'],
        resolvers: {
          query: withSecurity('pipelines', ['admin', 'user']),
          mutation: withSecurity('pipelineMutation', ['admin'])
        }
      }
    },
    i18n: withI18n(config.lang),
    seo: withSEO(),
    audit: withAudit(config.tenant),
    plugins: withPlugins('it_devops'),
    rgpd: true
  };
  return project;
}

module.exports = { generateProject };
