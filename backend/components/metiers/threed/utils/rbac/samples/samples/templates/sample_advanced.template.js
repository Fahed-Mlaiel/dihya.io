// sample_advanced.template.js - Template JS avancé RBAC
module.exports = (role = 'user') => ({
  role,
  allowed: role === 'admin' || (role === 'user')
});
