// rbac.js – Module RBAC ultra-modulaire pour tests métiers 3D
// Respecte la logique métier, la modularité et la conformité RGPD

const ROLES = ['admin', 'editor', 'viewer'];
const PERMISSIONS = {
  admin: ['read', 'write', 'delete', 'manage_users'],
  editor: ['read', 'write'],
  viewer: ['read']
};

function hasPermission(user, permission) {
  if (!user || !user.roles) return false;
  return user.roles.some(role => (PERMISSIONS[role] || []).includes(permission));
}

module.exports = { ROLES, PERMISSIONS, hasPermission };
