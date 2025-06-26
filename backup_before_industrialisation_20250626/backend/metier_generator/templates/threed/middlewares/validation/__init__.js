// Point d'entrée global pour tous les middlewares de validation du module threed
const input = require('./input');
const schema = require('./schema');

module.exports = {
  ...input,
  ...schema
};
