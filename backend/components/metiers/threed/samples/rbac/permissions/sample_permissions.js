// Exemple avancé permissions RBAC (Node.js)

module.exports = function hasPermission(user, permission) {
  if (!user || !user.permissions) {
    throw new Error('User or permissions are missing');
  }
  return user.permissions.includes(permission);
};
