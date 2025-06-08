// Exemple avancé d’accès (Node.js)
module.exports = function checkAccess(user, resource) {
  // Logique d’accès avancée
  return user && resource && user.roles.includes('admin');
};
