// Test avancé pour index.js du module samples
const samples = require('../../../../api/samples/index');
describe('Samples Index', () => {
  it('should expose expected API', () => {
    expect(samples).toBeDefined();
    // Ajouter des assertions avancées selon la logique métier
  });
});
