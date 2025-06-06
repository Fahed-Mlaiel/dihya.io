// index.js – Point d'entrée JS pour les utilitaires plugins du module threed
// Exporte toutes les fonctions principales et helpers (core, helpers, fallback)
module.exports = {
  ...require('./core/pluginManager'),
  ...require('./core/sample_plugin'),
  ...require('./helpers/plugins_helper'),
  ...require('./fallback/plugins_fallback')
};
