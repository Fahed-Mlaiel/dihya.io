// metrics.test.js – Tests unitaires pour metrics.js (Node.js/Jest)
const metrics = require('./metrics');

describe('Metrics', () => {
  it('record et getAverage fonctionnent', () => {
    metrics.record('test', 10);
    metrics.record('test', 20);
    expect(metrics.getAverage('test')).toBe(15);
  });
  it('getAll retourne toutes les métriques', () => {
    expect(metrics.getAll()).toHaveProperty('test');
  });
});
