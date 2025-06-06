// Point d’entrée professionnel du module services
const core = require('./core');
module.exports = {
  ...core,
  ServiceThreed: core.ServiceThreed,
  helpers: require('./helpers'),
  fallback: require('./fallback')
};
