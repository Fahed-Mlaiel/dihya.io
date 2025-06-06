// index.js – Point d'entrée JS pour les utilitaires metrics du module threed
// Exporte toutes les fonctions principales et helpers (core, helpers, fallback)
module.exports = {
  ...require('./core/metrics'),
  ...require('./helpers/metrics_helper'),
  ...require('./fallback/fallback')
};
