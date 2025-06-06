// sample_usage.test.js
// Tests unitaires avancés pour les exemples metrics JS
const metrics = require('../core/metrics');
const data = require('./sample_metrics_data.json').metrics;

describe('Sample usage metrics JS', () => {
  it('calcule correctement la moyenne', () => {
    expect(metrics.calculerMoyenne(data)).toBeCloseTo(15.814, 2);
  });
  it('calcule correctement la médiane', () => {
    expect(metrics.calculerMediane(data)).toBe(3.5);
  });
  it('gère les tableaux vides', () => {
    expect(() => metrics.calculerMoyenne([])).toThrow();
  });
});
