// Index clé en main pour tous les tests de middlewares de sécurité threed

const audit = require('./audit');
const auth = require('./auth');

module.exports = {
  ...audit,
  ...auth
};

// Utilisation :
// const securityTests = require('./security');
// securityTests.testAudit(...);
// securityTests.testAuth(...);
