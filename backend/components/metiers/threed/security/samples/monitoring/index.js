// Point d’entrée principal JS pour monitoring

module.exports = {
  alerts: require('./alerts'),
  grafana: require('./grafana'),
  prometheus: require('./prometheus')
};
