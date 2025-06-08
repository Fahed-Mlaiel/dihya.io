// Point d’entrée principal du module monitoring de sécurité
module.exports = {
  alerts: require('./alerts'),
  grafana: require('./grafana'),
  prometheus: require('./prometheus'),
  samples: require('./samples')
};
