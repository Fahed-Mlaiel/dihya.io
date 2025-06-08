// index.js - Point d'entrée centralisé ultra avancé pour tous les tests de monitoring

const alerts = require('./alerts');
const grafana = require('./grafana');
const prometheus = require('./prometheus');

module.exports = {
  alerts,
  grafana,
  prometheus,
  description: 'Index centralisé pour tous les tests de monitoring (alerts, grafana, prometheus).',
  meta: {
    domain: 'monitoring',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
