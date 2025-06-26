// Fonctions principales attendues par les tests
let metrics = [];
function recordMetric(name, value) {
  metrics.push({ name, value, timestamp: new Date().toISOString() });
  return true;
}
function getAverageMetric(name) {
  const filtered = metrics.filter(m => m.name === name);
  if (!filtered.length) return 0;
  return filtered.reduce((a, b) => a + b.value, 0) / filtered.length;
}
function getAllMetrics() {
  return metrics;
}

module.exports = {
  recordMetric,
  getAverageMetric,
  getAllMetrics
};
