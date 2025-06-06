// rbac_core.js
// Logique métier principale RBAC (JS)
function checkPermission(user, permission) {
  return user.permissions && user.permissions.includes(permission);
}
function getUserRoles(user) {
  return user.roles || [];
}
module.exports = { checkPermission, getUserRoles };
