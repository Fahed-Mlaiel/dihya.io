// rbac_templates.js - Templates métier RBAC (JS)
module.exports = (role = 'user') => ({
  permissions: role === 'admin' ? ['read', 'write', 'delete'] : role === 'user' ? ['read'] : []
});
