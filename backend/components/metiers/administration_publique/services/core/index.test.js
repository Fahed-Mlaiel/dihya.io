// index.test.js
// Test d'import du point d'entrée JS principal du module core services threed.

describe('index.js (core services threed)', () => {
  it('doit s\'importer sans erreur', () => {
    expect(() => require('./index')).not.toThrow();
  });
  it('doit exposer ApiService, ServicesController, ServicesHelper, ServiceThreed, SampleService', () => {
    const mod = require('./index');
    expect(mod.ApiService).toBeDefined();
    expect(mod.ServicesController).toBeDefined();
    expect(mod.ServicesHelper).toBeDefined();
    expect(mod.ServiceThreed).toBeDefined();
    expect(mod.SampleService).toBeDefined();
  });
});
