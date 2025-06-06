// Test d'import du module samples (JS)
const sample = require('.');
describe('helpers/core/samples/__init__.js', () => {
  it('doit exposer la fixture sample', () => {
    expect(sample.sample).toBeDefined();
    expect(sample.sample.name).toBe('Sample Helper');
  });
});
