// Point d’entrée ultra avancé pour scripts
const path = require('path');
module.exports = {
  audit: require(path.join(__dirname, 'audit')),
  backup: require(path.join(__dirname, 'backup')),
  compliance: require(path.join(__dirname, 'compliance')),
  restore: require(path.join(__dirname, 'restore'))
};
