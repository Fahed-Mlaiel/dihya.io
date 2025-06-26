// Index clé en main pour tous les tests de middlewares de contexte threed

const session = require('./session');
const trace = require('./trace');

module.exports = {
  ...session,
  ...trace
};

// Utilisation :
// const contextTests = require('./context');
// contextTests.testSession(...);
// contextTests.testTrace(...);
