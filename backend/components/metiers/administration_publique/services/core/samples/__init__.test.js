// __init__.test.js
// Test d'import du point d'entrée JS du sous-module samples

describe('__init__.js (samples)', () => {
  it('doit s\'importer sans erreur', () => {
    expect(() => require('./__init__')).not.toThrow();
  });
  it('doit exposer SampleService', () => {
    const mod = require('./__init__');
    expect(mod.SampleService).toBeDefined();
  });
});
