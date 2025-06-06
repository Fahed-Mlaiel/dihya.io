// index.js – Point d’entrée global des tests Threed
// Exporte les runners, helpers et intégration multi-modules
module.exports = {
  // Exemples d’exports (à adapter selon la logique métier)
  api: require('./api'),
  fixtures: require('./fixtures'),
  guides: require('./guides'),
  integration: require('./integration'),
  legacy: require('./legacy'),
  plugins: require('./plugins'),
  rgpd: require('./rgpd'),
  security: require('./security'),
  services: require('./services'),
  templates: require('./templates'),
  utils: require('./utils')
};
