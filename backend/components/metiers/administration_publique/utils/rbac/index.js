// index.js
// Point d'entrée JS global RBAC (expose core, helpers, fallback)
module.exports = {
  ...require('./core'),
  ...require('./helpers'),
  ...require('./fallback')
};
