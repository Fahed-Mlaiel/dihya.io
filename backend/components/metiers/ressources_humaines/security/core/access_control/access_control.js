// access_control.js – Contrôle d'accès centralisé

const { enforcePolicy } = require('../policy/policy');

function checkAccess(user, resource, action) {
  return enforcePolicy(user, action, resource);
}

module.exports = { checkAccess };
