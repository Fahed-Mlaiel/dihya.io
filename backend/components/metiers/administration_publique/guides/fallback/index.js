// index.js – Point d’entrée principal JS pour guides/fallback
module.exports = {
  ...require('./accessibility'),
  ...require('./plugins'),
  ...require('./services'),
  ...require('./samples'),
};
