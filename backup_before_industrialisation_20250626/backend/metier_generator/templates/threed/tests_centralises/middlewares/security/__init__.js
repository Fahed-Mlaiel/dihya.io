// Point d'entrée global pour tous les tests de middlewares de sécurité threed
const audit = require('./audit');
const auth = require('./auth');

module.exports = {
  ...audit,
  ...auth
};
