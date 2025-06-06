// Test d'import du module accessibility (JS)
const accessibility = require('./');
describe('guides/core/accessibility/__init__.js', () => {
  it('doit exposer les guides et samples d’accessibilité', () => {
    expect(typeof accessibility).toBe('object');
    expect(accessibility.getAccessibilityGuide).toBeDefined();
    expect(accessibility.sample).toBeDefined();
  });
});
