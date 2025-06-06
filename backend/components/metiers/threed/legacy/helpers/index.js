// index.js
// Point d'entrée principal JS pour le module legacy helpers.
// Permet l'import centralisé de tous les helpers legacy (core, validators, etc.).

module.exports = {
  ...require('./core'),
  ...require('./validators'),
};
