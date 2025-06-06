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
