// policy.js – Politiques de sécurité avancées

function enforcePolicy(user, action, resource) {
  if (user.isAdmin) return true;
  if (user.permissions && user.permissions.includes(action)) return true;
  return false;
}

module.exports = { enforcePolicy };
