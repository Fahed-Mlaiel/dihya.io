// service_threed.test.js – Tests unitaires JS pour service principal 3D
const service = require('./service_threed');
describe('Service principal 3D (JS)', () => {
  test('get3DModel retourne un modèle', () => {
    expect(service.get3DModel(1).id).toBe(1);
    expect(() => service.get3DModel()).toThrow('id requis');
  });
  test('list3DModels retourne 3 modèles', () => {
    expect(service.list3DModels().length).toBe(3);
  });
  test('auditModel fonctionne', () => {
    expect(service.auditModel({ id: 1 }).success).toBeTruthy();
    expect(() => service.auditModel({})).toThrow('id requis');
  });
  test('secureAccess contrôle l’accès', () => {
    expect(service.secureAccess({ role: 'admin' }, 'write')).toBeTruthy();
    expect(service.secureAccess({ role: 'user' }, 'read')).toBeTruthy();
    expect(() => service.secureAccess({ role: 'user' }, 'write')).toThrow('Accès refusé');
  });
});

const ServiceThreed = require('./service_threed');

describe('ServiceThreed', () => {
  it('doit s\'initialiser correctement', () => {
    const service = new ServiceThreed({ mode: 'test' });
    expect(service.options).toEqual({ mode: 'test' });
    expect(service.getAuditTrail()).toEqual([]);
  });

  it('doit initialiser la config et auditer', () => {
    const service = new ServiceThreed();
    expect(service.init({ version: 1 })).toBe(true);
    expect(service.config).toEqual({ version: 1 });
    expect(service.getAuditTrail()[0].action).toBe('init');
  });

  it('doit traiter une opération valide et auditer', () => {
    const service = new ServiceThreed();
    service.init({ version: 2 });
    const result = service.process('OP', { foo: 'bar' });
    expect(result).toEqual({ success: true, operation: 'OP', data: { foo: 'bar' }, config: { version: 2 } });
    expect(service.getAuditTrail().length).toBe(2);
    expect(service.getAuditTrail()[1].action).toBe('process');
  });

  it('doit lever une erreur sur une opération invalide et auditer', () => {
    const service = new ServiceThreed();
    expect(() => service.process(null, {})).toThrow('Invalid operation');
    expect(service.getAuditTrail()[0].action).toBe('error');
  });
});
