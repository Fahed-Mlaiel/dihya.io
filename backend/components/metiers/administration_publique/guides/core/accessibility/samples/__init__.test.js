// Test d'import du module samples (JS)
const sample = require('./');
describe('guides/core/accessibility/samples/__init__.js', () => {
  it('doit exposer la fixture sample', () => {
    expect(sample.sample).toBeDefined();
    expect(sample.sample.name).toBe('Sample Accessibility Guide');
  });
});
