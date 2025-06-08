// sample_policy.js – Exemple de politique sécurité clé en main

function getSamplePolicy() {
  return {
    name: 'Sécurité 3D',
    version: '1.0',
    rules: [
      'Accès restreint par rôles',
      'Chiffrement des données',
      'Audit et monitoring',
      'Conformité RGPD'
    ]
  };
}

module.exports = { getSamplePolicy };
