// index.test.js – Test d’intégration du point d’entrée JS guides/core
describe('Entrée JS guides/core', () => {
  const entry = require('./index.js');
  it('expose tous les sous-modules critiques', () => {
    expect(entry.accessibility).toBeDefined();
    expect(entry.fixtures).toBeDefined();
    expect(entry.plugins).toBeDefined();
    expect(entry.services).toBeDefined();
    expect(entry.utils).toBeDefined();
    expect(entry.views).toBeDefined();
  });
});
