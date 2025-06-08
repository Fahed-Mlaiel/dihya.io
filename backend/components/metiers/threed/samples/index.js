// Point d’entrée ultra avancé pour samples
const path = require('path');
module.exports = {
  access: require(path.join(__dirname, 'access')),
  audit: require(path.join(__dirname, 'audit')),
  compliance: require(path.join(__dirname, 'compliance')),
  helpers: require(path.join(__dirname, 'helpers')),
  monitoring: require(path.join(__dirname, 'monitoring')),
  policy: require(path.join(__dirname, 'policy')),
  rbac: require(path.join(__dirname, 'rbac')),
  rgpd: require(path.join(__dirname, 'rgpd')),
  scripts: require(path.join(__dirname, 'scripts')),
  validators: require(path.join(__dirname, 'validators'))
};
