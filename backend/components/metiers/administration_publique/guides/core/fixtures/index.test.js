// index.test.js – Test d’intégration du point d’entrée JS fixtures
describe('Entrée JS fixtures', () => {
  const entry = require('./index.js');
  it('expose guides et samples', () => {
    expect(entry.guides).toBeDefined();
    expect(entry.samples).toBeDefined();
  });
});
