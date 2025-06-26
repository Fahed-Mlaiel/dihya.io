// Point d'entrée global pour tous les middlewares de sécurité du module threed
const audit = require('./audit');
const auth = require('./auth');

module.exports = {
  ...audit,
  ...auth
};
