// __init__.js – RBAC sécurité 3D

module.exports = {
  ...require('./roles'),
  ...require('./permissions'),
  ...require('./rbac_engine'),
};
