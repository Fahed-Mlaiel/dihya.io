// Helpers d’accès (MFA, SSO, provisioning, logs, audit, validation) – clé en main
const { generateMfaToken, provisionUser } = require('./mfa/helpers_access');
const { initiateSsoLogin } = require('./sso/sso_helper');
const { logAccessEvent, validateAccessPolicy } = require('./audit/advanced_access_helper');

module.exports = {
  generateMfaToken,
  provisionUser,
  initiateSsoLogin,
  logAccessEvent,
  validateAccessPolicy
};

// Exemple d’utilisation :
// const { generateMfaToken, initiateSsoLogin } = require('./helpers');
// const token = generateMfaToken('user1');
// const sso = initiateSsoLogin('google', 'https://app.dihya.io/callback');

// Redirige vers index.js pour un point d’entrée unique et clé en main
module.exports = require('./index');
