// index.test.js – Test d’intégration du point d’entrée JS plugins guides/core
describe('Entrée JS plugins guides/core', () => {
  const entry = require('./index.js');
  it('expose la fonction getPluginsGuide', () => {
    expect(entry.getPluginsGuide).toBeDefined();
  });
});
