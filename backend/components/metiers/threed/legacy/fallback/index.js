// index.js – Point d’entrée avancé du module legacy/fallback
module.exports = {
  ...require('./migrations'),
  ...require('./mocks')
};
