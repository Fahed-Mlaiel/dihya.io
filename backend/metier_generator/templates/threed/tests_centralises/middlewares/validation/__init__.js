// Point d'entrée global pour tous les tests de middlewares de validation threed
const input = require('./input');
const schema = require('./schema');

module.exports = {
  ...input,
  ...schema
};
