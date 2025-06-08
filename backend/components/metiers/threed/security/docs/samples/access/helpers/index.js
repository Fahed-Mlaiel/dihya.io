// index.js
// Point d’entrée principal pour tous les helpers d’accès (clé en main)

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

// Utilisation :
// const helpers = require('./index');
// helpers.generateMfaToken('user1');
// helpers.initiateSsoLogin('google', 'https://app.dihya.io/callback');
// helpers.logAccessEvent('user1', 'LOGIN', { ip: '127.0.0.1' });
