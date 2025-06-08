// __init__.js - Point d'entrée ultra avancé pour les tests de monitoring

const alerts = require('./alerts');
const grafana = require('./grafana');
const prometheus = require('./prometheus');

module.exports = {
  alerts,
  grafana,
  prometheus,
  description: 'Module centralisé pour les tests de monitoring (alerts, grafana, prometheus).',
  meta: {
    domain: 'monitoring',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
