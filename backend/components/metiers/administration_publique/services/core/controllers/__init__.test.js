// __init__.test.js
// Test d'import du point d'entrée JS du sous-module controllers

describe('__init__.js (controllers)', () => {
  it('doit s\'importer sans erreur', () => {
    expect(() => require('./__init__')).not.toThrow();
  });
  it('doit exposer ServicesController', () => {
    const mod = require('./__init__');
    expect(mod.ServicesController).toBeDefined();
  });
});
