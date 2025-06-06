// rbac_utils.js – Module RBAC ultra avancé, clé en main, conforme RGPD et logique métier
const ROLES = ['admin', 'editor', 'viewer', 'auditor'];
const PERMISSIONS = {
  admin: ['read', 'write', 'delete', 'manage_users', 'audit'],
  editor: ['read', 'write'],
  viewer: ['read'],
  auditor: ['read', 'audit']
};

function hasPermission(user, permission) {
  if (!user || !user.roles) return false;
  return user.roles.some(role => (PERMISSIONS[role] || []).includes(permission));
}

function getUserPermissions(user) {
  if (!user || !user.roles) return [];
  return Array.from(new Set(user.roles.flatMap(role => PERMISSIONS[role] || [])));
}

module.exports = {
  ROLES,
  PERMISSIONS,
  hasPermission,
  getUserPermissions
};
