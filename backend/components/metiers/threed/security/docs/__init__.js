// __init__.js – Documentation technique & guides Security 3D
// Point d’entrée modulaire pour tous les guides, intégrations et modèles de politiques

const guides = require('./guides');
const integration = require('./integration');
const policies = require('./policies');

module.exports = {
  guides,
  integration,
  policies,
};
