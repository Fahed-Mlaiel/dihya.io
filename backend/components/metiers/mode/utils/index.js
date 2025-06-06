// Point d'entrée JS pour les utilitaires environnement
// Permet d'exposer les fonctions d'audit, i18n, et autres utilitaires côté Node.js

const audit = require('./audit');
const i18n = require('./i18n');

module.exports = {
  audit,
  i18n,
  // Ajouter d'autres utilitaires JS ici si besoin
};
