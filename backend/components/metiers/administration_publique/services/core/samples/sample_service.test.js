// sample_service.test.js
// Tests unitaires pour SampleService (clé en main, CI/CD ready)

const SampleService = require('./sample_service');

describe('SampleService', () => {
  it('doit s\'initialiser correctement', () => {
    const service = new SampleService({ mode: 'test' });
    expect(service.options).toEqual({ mode: 'test' });
    expect(service.state).toBe('ready');
  });

  it('doit initialiser la config', () => {
    const service = new SampleService();
    expect(service.init({ level: 1 })).toBe(true);
    expect(service.config).toEqual({ level: 1 });
    expect(service.state).toBe('initialized');
  });

  it('doit exécuter le run sample', () => {
    const service = new SampleService();
    service.init({ level: 2 });
    const result = service.run('DATA');
    expect(result).toEqual({ processed: true, data: 'DATA', config: { level: 2 }, state: 'initialized' });
  });
});
