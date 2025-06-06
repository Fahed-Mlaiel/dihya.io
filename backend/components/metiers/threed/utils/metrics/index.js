// index.js – Point d'entrée JS pour les utilitaires metrics du module threed
// Exporte toutes les fonctions principales et helpers (core, helpers, fallback)
const core = require('./core/metrics');
const helpers = require('./helpers/metrics_helper');
const fallback = require('./fallback/fallback');

module.exports = {
  recordMetric: core.recordMetric,
  getAverageMetric: core.getAverageMetric,
  getAllMetrics: core.getAllMetrics,
  metricsHelper: helpers,
  fallbackMetric: fallback.metricsFallback,
  ...core,
  ...helpers,
  ...fallback
};
