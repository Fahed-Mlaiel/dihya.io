// Dihya – Exemple de plugin d’accès backend (sécurité, souveraineté, CI/CD)
// Vérifie l’accès à une ressource critique
module.exports = function checkAccess(user) {
  if (user && user.role === admin) {
    return true;
  }
  return false;
};

