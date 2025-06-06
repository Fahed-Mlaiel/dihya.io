// __init__.js – Point d’entrée JS pour guides/helpers
module.exports = {
  ...require('./accessibility'),
  ...require('./plugins'),
  ...require('./services'),
};
