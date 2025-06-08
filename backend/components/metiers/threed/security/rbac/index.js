// Point d’entrée principal du module RBAC de sécurité
module.exports = {
  engine: require('./engine'),
  roles: require('./roles'),
  permissions: require('./permissions'),
  samples: require('./samples')
};
