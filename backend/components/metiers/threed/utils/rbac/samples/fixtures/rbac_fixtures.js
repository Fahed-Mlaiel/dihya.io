// rbac_fixtures.js - Fixtures métier RBAC (JS)
module.exports = {
  admin: { permissions: ['read', 'write', 'delete'] },
  user: { permissions: ['read'] },
  guest: { permissions: [] }
};
