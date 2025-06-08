// __init__.js - Point d'entrée ultra avancé pour les tests d'intégration Grafana

const fs = require('fs');
const path = require('path');

const tests = fs.readdirSync(__dirname)
  .filter(f => f.startsWith('sample_grafana') && f.endsWith('.js'))
  .reduce((acc, f) => {
    acc[path.basename(f, '.js')] = require(path.join(__dirname, f));
    return acc;
  }, {});

module.exports = {
  ...tests,
  description: 'Module centralisé pour les tests d’intégration Grafana (dashboards, alertes, monitoring visuel).',
  meta: {
    domain: 'monitoring',
    subdomain: 'grafana',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
