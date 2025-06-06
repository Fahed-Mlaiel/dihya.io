// __init__.test.js
// Test d'import du point d'entrée JS du sous-module helpers

describe('__init__.js (helpers)', () => {
  it('doit s\'importer sans erreur', () => {
    expect(() => require('./__init__')).not.toThrow();
  });
  it('doit exposer ServicesHelper', () => {
    const mod = require('./__init__');
    expect(mod.ServicesHelper).toBeDefined();
  });
});
