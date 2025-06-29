// rbac_sample.js – Exemple de RBAC ultra avancé
/**
 * Simule un contrôle RBAC legacy Voyage
 */
function rbacSample(user, role) {
  // ... logique RBAC avancée ...
  return role === 'admin' ? `${user} a tous les droits` : `${user} accès restreint`;
}

module.exports = rbacSample;
