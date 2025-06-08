// index.js – Point d'entrée racine pour les tests centralisés de l'API Threed
// Ce fichier permet d'agréger et d'exposer les modules de test pour la CI/CD, l'auto-discovery et l'import facilité.

module.exports = {
  accessibility: require('./accessibility'),
  audit: require('./audit'),
  controllers: require('./controllers'),
  core: require('./core'),
  db: require('./db'),
  hooks: require('./hooks'),
  middlewares: require('./middlewares'),
  rgpd: require('./rgpd'),
  samples: require('./samples'),
  validators: require('./validators'),
  // Ajouter ici tout nouveau sous-module de test centralisé
};

// Découverte et exécution automatique de tous les tests JS du dossier API (récursif)
const { discoverAllTestsRecursively } = require('./__init__.js');
const path = require('path');
discoverAllTestsRecursively(__dirname).forEach(testFile => {
  require(path.resolve(testFile));
});
console.log('Tous les tests API Threed ont été découverts et exécutés.');
