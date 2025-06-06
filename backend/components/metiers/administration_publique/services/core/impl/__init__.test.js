// __init__.test.js
// Test d'import du point d'entrée JS du sous-module impl

describe('__init__.js (impl)', () => {
  it('doit s\'importer sans erreur', () => {
    expect(() => require('./__init__')).not.toThrow();
  });
  it('doit exposer ServiceThreed', () => {
    const mod = require('./__init__');
    expect(mod.ServiceThreed).toBeDefined();
  });
});
