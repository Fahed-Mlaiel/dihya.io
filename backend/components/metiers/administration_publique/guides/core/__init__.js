// __init__.js – Point d’entrée JS du sous-module guides/core
// Exporte tous les sous-modules thématiques (accessibility, fixtures, plugins, services, utils, views)
// Synchronisé avec __init__.py
module.exports = {
  ...require('./accessibility'),
  ...require('./fixtures'),
  ...require('./plugins'),
  ...require('./services'),
  ...require('./utils'),
  ...require('./views')
};
