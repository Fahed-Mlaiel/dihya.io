// sample_usage.js - Exemple d'utilisation RBAC
function checkPermission(user, permission) {
  return user && user.permissions && user.permissions.includes(permission);
}
module.exports = checkPermission;
