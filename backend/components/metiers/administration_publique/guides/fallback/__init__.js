// __init__.js – Point d’entrée JS pour guides/fallback
module.exports = {
  ...require('./accessibility'),
  ...require('./plugins'),
  ...require('./services'),
  ...require('./samples'),
};
