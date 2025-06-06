// services_helper.test.js – Tests unitaires JS pour helpers services Threed
const helper = require('./services_helper');
describe('Helpers services Threed (JS)', () => {
  test('getServiceStatus retourne ok', () => {
    expect(helper.getServiceStatus().status).toBe('ok');
  });
  test('simulateHeavyLoad génère 10000 caractères', () => {
    expect(helper.simulateHeavyLoad().length).toBe(10000);
  });
  test('auditService retourne un audit', () => {
    expect(helper.auditService('test')).toContain('Audit avancé');
  });
  test('simulateExtremeLoad génère 100000 caractères', () => {
    expect(helper.simulateExtremeLoad().length).toBe(100000);
  });
  test('checkAccess contrôle les droits', () => {
    expect(helper.checkAccess({ role: 'admin' }, 'write')).toBeTruthy();
    expect(helper.checkAccess({ role: 'user' }, 'read')).toBeTruthy();
    expect(helper.checkAccess({ role: 'user' }, 'write')).toBeFalsy();
  });
});

const ServicesHelper = require('./services_helper');

describe('ServicesHelper', () => {
  it('doit s\'initialiser correctement', () => {
    const helper = new ServicesHelper({ mode: 'test' });
    expect(helper.options).toEqual({ mode: 'test' });
    expect(helper.getAuditTrail()).toEqual([]);
  });

  it('doit initialiser la config et auditer', () => {
    const helper = new ServicesHelper();
    expect(helper.init({ version: 1 })).toBe(true);
    expect(helper.config).toEqual({ version: 1 });
    expect(helper.getAuditTrail()[0].action).toBe('init');
  });

  it('doit assister une opération valide et auditer', () => {
    const helper = new ServicesHelper();
    helper.init({ version: 2 });
    const result = helper.assist('OP', { foo: 'bar' });
    expect(result).toEqual({ success: true, operation: 'OP', data: { foo: 'bar' }, config: { version: 2 } });
    expect(helper.getAuditTrail().length).toBe(2);
    expect(helper.getAuditTrail()[1].action).toBe('assist');
  });

  it('doit lever une erreur sur une opération invalide et auditer', () => {
    const helper = new ServicesHelper();
    expect(() => helper.assist(null, {})).toThrow('Invalid operation');
    expect(helper.getAuditTrail()[0].action).toBe('error');
  });
});
