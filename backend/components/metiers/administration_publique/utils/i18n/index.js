// index.js – Point d'entrée JS pour les utilitaires i18n du module threed
module.exports = {
  ...require('./core'),
  ...require('./helpers'),
  ...require('./fallback'),
  ...require('./samples'),
};
