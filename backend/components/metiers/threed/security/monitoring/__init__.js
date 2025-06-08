// Monitoring sécurité – clé en main
const alerts = require('./alerts/alerts');
const grafana = require('./grafana/grafana');
const prometheus = require('./prometheus/prometheus');

module.exports = {
  alerts,
  grafana,
  prometheus
};
