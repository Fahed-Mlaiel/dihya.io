// Point d’entrée ultra avancé pour validators
const path = require('path');
module.exports = {
  input: require(path.join(__dirname, 'input')),
  rgpd: require(path.join(__dirname, 'rgpd'))
};
