// index.js
// Point d'entrée principal JS pour le module legacy helpers/validators.
// Permet l'import centralisé de tous les helpers/validators legacy (core, samples, etc.).

module.exports = {
  ...require('./core'),
  ...require('./samples'),
};
