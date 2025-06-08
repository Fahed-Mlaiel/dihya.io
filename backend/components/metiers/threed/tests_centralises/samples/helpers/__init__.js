// __init__.js - Point d'entrée ultra avancé pour les tests helpers

const logger = require('./logger');
const utils = require('./utils');

module.exports = {
  logger,
  utils,
  description: 'Module centralisé pour les tests helpers (logger, utils).',
  meta: {
    domain: 'helpers',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
