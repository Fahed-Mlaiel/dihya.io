// services_controller.test.js
// Tests unitaires ultra avancés pour ServicesController (clé en main, CI/CD ready)

const ServicesController = require('./services_controller');

describe('ServicesController', () => {
  it('doit s\'initialiser correctement', () => {
    const ctrl = new ServicesController({ mode: 'test' });
    expect(ctrl.options).toEqual({ mode: 'test' });
    expect(ctrl.getAuditTrail()).toEqual([]);
  });

  it('doit initialiser la config et auditer', () => {
    const ctrl = new ServicesController();
    expect(ctrl.init({ version: 1 })).toBe(true);
    expect(ctrl.config).toEqual({ version: 1 });
    expect(ctrl.getAuditTrail()[0].action).toBe('init');
  });

  it('doit gérer une action valide et auditer', () => {
    const ctrl = new ServicesController();
    ctrl.init({ version: 2 });
    const result = ctrl.handle('ACTION', { foo: 'bar' });
    expect(result).toEqual({ success: true, action: 'ACTION', payload: { foo: 'bar' }, config: { version: 2 } });
    expect(ctrl.getAuditTrail().length).toBe(2);
    expect(ctrl.getAuditTrail()[1].action).toBe('handle');
  });

  it('doit lever une erreur sur une action invalide et auditer', () => {
    const ctrl = new ServicesController();
    expect(() => ctrl.handle(null, {})).toThrow('Invalid action');
    expect(ctrl.getAuditTrail()[0].action).toBe('error');
  });
});
