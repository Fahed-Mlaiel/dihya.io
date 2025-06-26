// Exemple avancé rôles RBAC (Node.js)

module.exports = function hasRole(user, role) {
  return user.roles.includes(role);
};
