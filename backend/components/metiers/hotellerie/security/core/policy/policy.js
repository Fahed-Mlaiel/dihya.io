// policy.js – Politiques de sécurité avancées

function enforcePolicy(user, action) {
  // Vérification de sécurité : user ne doit pas être null/undefined
  if (!user) return false;

  // Utilisation de resource possible selon la logique métier future
  if (user.isAdmin) return true;
  if (user?.permissions && user?.permissions.includes(action)) return true;
  return false;
}

module.exports = { enforcePolicy };
