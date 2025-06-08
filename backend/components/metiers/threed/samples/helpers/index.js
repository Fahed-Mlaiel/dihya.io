// Point d’entrée ultra avancé pour helpers
const path = require('path');
module.exports = {
  logger: require(path.join(__dirname, 'logger')),
  utils: require(path.join(__dirname, 'utils'))
};
