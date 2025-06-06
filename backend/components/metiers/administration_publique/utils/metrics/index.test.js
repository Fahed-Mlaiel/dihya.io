// index.test.js – Test d'intégration du point d'entrée metrics JS (conformité, CI/CD)
const metrics = require('./index');
describe('Entrée JS metrics utils threed', () => {
  it('doit exposer recordMetric, getAverageMetric, getAllMetrics, helpers et fallback', () => {
    expect(metrics).toHaveProperty('recordMetric');
    expect(metrics).toHaveProperty('getAverageMetric');
    expect(metrics).toHaveProperty('getAllMetrics');
    expect(metrics).toHaveProperty('metricsHelper');
    expect(metrics).toHaveProperty('fallbackMetric');
  });
});
