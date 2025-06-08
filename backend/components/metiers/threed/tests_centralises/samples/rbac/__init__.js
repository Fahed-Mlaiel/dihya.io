// __init__.js - Point d'entrée ultra avancé pour les tests RBAC

const engine = require('./engine');
const permissions = require('./permissions');
const roles = require('./roles');

module.exports = {
  engine,
  permissions,
  roles,
  description: 'Module centralisé pour les tests RBAC (engine, permissions, roles).',
  meta: {
    domain: 'rbac',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
