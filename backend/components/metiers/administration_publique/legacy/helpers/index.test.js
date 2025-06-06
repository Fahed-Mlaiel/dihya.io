// index.test.js
// Test d'import du point d'entrée JS principal du module legacy helpers.

describe('index.js (legacy helpers)', () => {
  it('doit s\'importer sans erreur', () => {
    expect(() => require('./index')).not.toThrow();
  });
});
