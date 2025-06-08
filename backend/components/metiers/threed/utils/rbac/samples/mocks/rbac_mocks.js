// rbac_mocks.js - Mocks métier RBAC (JS)
module.exports = {
  admin: { permissions: ['read', 'write', 'delete'] },
  user: { permissions: ['read'] },
  guest: { permissions: [] }
};
