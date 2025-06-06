// __init__.test.js
// Test d'import du point d'entrée JS du sous-module api

describe('__init__.js (api)', () => {
  it('doit s\'importer sans erreur', () => {
    expect(() => require('./__init__')).not.toThrow();
  });
  it('doit exposer ApiService', () => {
    const mod = require('./__init__');
    expect(mod.ApiService).toBeDefined();
  });
});
