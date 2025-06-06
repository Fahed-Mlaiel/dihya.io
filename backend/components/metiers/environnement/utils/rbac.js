// rbac.js – Contrôle d'accès basé sur les rôles (Node.js)
module.exports = function checkPermission(user, action) {
  // admin a tous les droits, les autres seulement lecture
  return user === 'admin' || action === 'read';
};
