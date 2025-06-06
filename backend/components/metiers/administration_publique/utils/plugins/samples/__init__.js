// __init__.js
// Point d'entrée JS pour le dossier samples plugins (tous sous-modules)
module.exports = {
  sample: require('./pluginManager.sample.js'),
  test: require('./pluginManager.test.js')
};
