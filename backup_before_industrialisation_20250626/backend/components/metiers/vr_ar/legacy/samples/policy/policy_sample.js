// policy_sample.js – Exemple de politique ultra avancé
/**
 * Simule une politique de sécurité legacy vr_ar
 */
function policySample(user) {
  // ... logique de politique avancée ...
  return user === 'admin' ? 'full-access' : 'restricted';
}

module.exports = policySample;
