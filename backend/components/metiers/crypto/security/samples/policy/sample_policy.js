// Exemple avancé de gestion de politique (Node.js)
function applyPolicy(policy) {
  // Logique d’application de politique
  if (typeof policy === 'string' && policy.includes('@')) {
    return 'Politique appliquée.';
  }
  return `Politique ${policy} appliquée.`;
}

module.exports = { applyPolicy };
