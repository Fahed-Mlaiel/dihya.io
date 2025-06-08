// index.js
// Point d’entrée principal pour tous les exemples d’intégration d’accès (clé en main)

const sampleAccess = require('./mfa/sample_access');
const sampleSso = require('./sso/sample_sso');

module.exports = {
  ...sampleAccess,
  ...sampleSso
};

// Utilisation :
// const samples = require('./index');
// samples.<fonction_exemple>()
// Voir chaque fichier pour des scénarios concrets.
