// Exemple avancé moteur RBAC (Node.js)

module.exports = function rbacEngine(user, action) {
  // Logique RBAC avancée
  return user.roles.includes('admin') || action === 'read';
};
