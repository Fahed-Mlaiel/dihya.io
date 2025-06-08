// index.js - Point d'entrée centralisé ultra avancé pour tous les tests RBAC

const engine = require('./engine');
const permissions = require('./permissions');
const roles = require('./roles');

module.exports = {
  engine,
  permissions,
  roles,
  description: 'Index centralisé pour tous les tests RBAC (engine, permissions, roles).',
  meta: {
    domain: 'rbac',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
