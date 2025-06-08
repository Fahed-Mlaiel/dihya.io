// Point d’entrée ultra avancé pour RBAC
const path = require('path');
module.exports = {
  engine: require(path.join(__dirname, 'engine')),
  permissions: require(path.join(__dirname, 'permissions')),
  roles: require(path.join(__dirname, 'roles'))
};
