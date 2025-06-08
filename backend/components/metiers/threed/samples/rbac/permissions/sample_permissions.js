// Exemple avancé permissions RBAC (Node.js)

module.exports = function hasPermission(user, permission) {
  return user.permissions.includes(permission);
};
