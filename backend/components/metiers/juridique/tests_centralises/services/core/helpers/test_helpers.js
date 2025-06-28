const { ServicesHelper } = require('../../../../services/core/helpers/services_helper');

// Test ultra avancé pour helpers services core (JS)
describe('Helpers Services Core', () => {
  it('initialise le helper et audite', () => {
    const helper = new ServicesHelper({ mode: 'prod' });
    expect(helper.init({ version: 1 })).toBe(true);
    expect(helper.config).toEqual({ version: 1 });
    expect(helper.getAuditTrail().length).toBe(1);
  });

  it('assist exécute une opération métier et audite', () => {
    const helper = new ServicesHelper();
    helper.init({});
    const result = helper.assist('op', { foo: 'bar' });
    expect(result.success).toBe(true);
    expect(result.operation).toBe('op');
    expect(result.data).toEqual({ foo: 'bar' });
    expect(helper.getAuditTrail().pop().action).toBe('assist');
  });

  it('assist lève une erreur sur opération invalide', () => {
    const helper = new ServicesHelper();
    helper.init({});
    expect(() => helper.assist('', {})).toThrow('Invalid operation');
    expect(helper.getAuditTrail().pop().action).toBe('error');
  });
});
