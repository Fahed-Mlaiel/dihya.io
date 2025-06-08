// __init__.js - Point d'entrée ultra avancé pour les tests d'intégration Prometheus

const fs = require('fs');
const path = require('path');

const tests = fs.readdirSync(__dirname)
  .filter(f => f.startsWith('sample_prometheus') && f.endsWith('.js'))
  .reduce((acc, f) => {
    acc[path.basename(f, '.js')] = require(path.join(__dirname, f));
    return acc;
  }, {});

module.exports = {
  ...tests,
  description: 'Module centralisé pour les tests d’intégration Prometheus (métriques, alertes, export).',
  meta: {
    domain: 'monitoring',
    subdomain: 'prometheus',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
