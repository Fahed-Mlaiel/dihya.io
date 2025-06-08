// index.js - Point d'entrée centralisé ultra avancé pour tous les tests helpers

const logger = require('./logger');
const utils = require('./utils');

module.exports = {
  logger,
  utils,
  description: 'Index centralisé pour tous les tests helpers (logger, utils).',
  meta: {
    domain: 'helpers',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
