// index.test.js - Test d'intégration pour index.js (accessibility)
const accessibility = require('./index');
describe('guides/core/accessibility/index.js', () => {
  it('doit exposer les guides principaux', () => {
    expect(typeof accessibility.getAccessibilityGuide).toBe('function');
  });
  it('doit exposer la fixture sample', () => {
    expect(accessibility.sample).toBeDefined();
    expect(accessibility.sample.name).toBe('Sample Accessibility Guide');
  });
});
