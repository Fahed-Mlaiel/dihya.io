// Point d’entrée ultra avancé pour monitoring
const path = require('path');
module.exports = {
  alerts: require(path.join(__dirname, 'alerts')),
  grafana: require(path.join(__dirname, 'grafana')),
  prometheus: require(path.join(__dirname, 'prometheus'))
};
