// Exemple avancé de politique (Node.js)

module.exports = function enforcePolicy(user, policy) {
  // Logique de politique avancée
  return policy.allowedUsers.includes(user.id);
};
