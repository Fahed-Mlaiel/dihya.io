// policy_model.js – Modèle de politique sécurité

function getPolicyModel() {
  return {
    name: 'Sécurité immobilier',
    version: '1.0',
    rules: [
      'Accès restreint par rôles',
      'Chiffrement des données',
      'Audit et monitoring',
      'Conformité RGPD'
    ]
  };
}

module.exports = { getPolicyModel };
