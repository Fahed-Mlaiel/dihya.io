// index.test.js
// Test d'import du point d'entrée JS principal du module legacy threed.

describe('index.js (legacy threed)', () => {
  it('doit s\'importer sans erreur', () => {
    expect(() => require('./index')).not.toThrow();
  });
});
