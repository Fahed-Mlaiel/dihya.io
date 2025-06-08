// Point d’entrée principal JS pour RBAC

module.exports = {
  engine: require('./engine'),
  permissions: require('./permissions'),
  roles: require('./roles')
};
