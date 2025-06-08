// index.js
// Point d’entrée principal pour tous les modules de documentation sécurité (clé en main)

const guides = require('./guides');
const integration = require('./integration');
const policies = require('./policies');
const samples = require('./samples');

module.exports = {
  guides,
  integration,
  policies,
  samples
};

// Utilisation :
// const docs = require('./index');
// docs.guides.<fonction_ou_guide>()
// docs.samples.access.generateMfaToken(...)
// ...
