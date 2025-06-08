// index.js - Point d'entrée des samples core
// Permet l'import modulaire de tous les exemples avancés (policies, crypto, access_control)

const policies = require('./policies');
const crypto = require('./crypto');
const accessControl = require('./access_control');

module.exports = {
  policies,
  crypto,
  accessControl
};
