// index.js
// Point d'entrée principal JS pour le module legacy threed.
// Permet l'import centralisé de tous les sous-modules legacy (core, fallback, helpers, etc.).

module.exports = {
  ...require('./core'),
  ...require('./fallback'),
  ...require('./helpers'),
};
