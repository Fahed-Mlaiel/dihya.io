// Index clé en main pour tous les tests de middlewares de validation threed

const input = require('./input');
const schema = require('./schema');

module.exports = {
  ...input,
  ...schema
};

// Utilisation :
// const validationTests = require('./validation');
// validationTests.testThreedInput(...);
// validationTests.testThreedSchema(...);
