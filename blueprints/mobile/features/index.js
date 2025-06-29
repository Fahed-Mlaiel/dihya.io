// index.js
// Exporte tous les features métiers

module.exports = {
  auth: require('./auth'),
  dashboard: require('./dashboard'),
  docs: require('./docs'),
  generation: require('./generation'),
  marketplace: require('./marketplace'),
  plugins: require('./plugins'),
  user: require('./user')
};
