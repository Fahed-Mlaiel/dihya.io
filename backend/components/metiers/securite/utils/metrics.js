// metrics.js – Collecte et reporting des métriques environnementales (Node.js)
const metrics = {};

module.exports = {
  record: (name, value) => {
    metrics[name] = (metrics[name] || []).concat([value]);
  },
  getAverage: (name) => {
    const arr = metrics[name] || [];
    if (!arr.length) return null;
    return arr.reduce((a, b) => a + b, 0) / arr.length;
  },
  getAll: () => metrics
};
