// Point d'entrée global pour tous les tests de middlewares de contexte threed
const session = require('./session');
const trace = require('./trace');

module.exports = {
  ...session,
  ...trace
};
