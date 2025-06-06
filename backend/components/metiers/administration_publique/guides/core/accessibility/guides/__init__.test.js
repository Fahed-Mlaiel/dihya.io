// Test d'import du module guides (JS)
const guide = require('./');
describe('guides/core/accessibility/guides/__init__.js', () => {
  it('doit exposer les guides d’accessibilité', () => {
    expect(typeof guide).toBe('object');
    expect(guide.getAccessibilityGuide).toBeDefined();
  });
});
