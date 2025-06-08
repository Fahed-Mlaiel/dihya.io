// __init__.js – RBAC sécurité 3D

// RBAC sécurité – clé en main
const engine = require('./engine/rbac_engine');
const roles = require('./roles/roles');
const permissions = require('./permissions/permissions');

module.exports = {
  engine,
  roles,
  permissions
};
