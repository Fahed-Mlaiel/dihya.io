// fallback.js
// Fallback metrics JS pour Recherche – exemple clé en main

/**
 * Fallback minimal : stocke une métrique en mémoire si la persistance échoue
 * @param {string} name
 * @param {number} value
 * @returns {object}
 */
const fallbackMetrics = [];
function metricsFallback(name, value) {
  const metric = {
    timestamp: new Date().toISOString(),
    name,
    value
  };
  fallbackMetrics.push(metric);
  return metric;
}

module.exports = { metricsFallback, fallbackMetrics };
