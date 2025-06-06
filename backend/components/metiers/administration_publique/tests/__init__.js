// __init__.js – Point d’entrée JS racine tests Threed

module.exports = {
  ...require('./api'),
  ...require('./fixtures'),
  ...require('./guides'),
  ...require('./integration'),
  ...require('./legacy'),
  ...require('./plugins'),
  ...require('./rgpd'),
  ...require('./security'),
  ...require('./services'),
  ...require('./templates'),
  ...require('./utils'),
};
