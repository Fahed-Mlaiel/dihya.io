// Exemple avancé d'accès (Node.js)
module.exports = function checkAccess(user, resource) {
  if (!user || !resource) return false;
  if (!user.roles || !Array.isArray(user.roles)) return false;
  return user.roles.includes('admin');
};
