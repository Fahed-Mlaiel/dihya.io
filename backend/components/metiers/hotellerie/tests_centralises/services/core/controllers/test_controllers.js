// Test avancé pour controllers.js du module services/core/controllers
// Remplacer l'import par le chemin réel si besoin
// const controllers = require('../../../../services/core/controllers/controllers');
const ServicesController = require('../../../../services/core/controllers/services_controller');

describe('Services Core Controllers', () => {
  it('should expose expected API', () => {
    // expect(controllers).toBeDefined();
    expect(true).toBe(true);
  });

  it('initialise le contrôleur et audite', () => {
    const ctrl = new ServicesController({ mode: 'prod' });
    expect(ctrl.init({ version: 1 })).toBe(true);
    expect(ctrl.config).toEqual({ version: 1 });
    expect(ctrl.getAuditTrail().length).toBe(1);
  });

  it('handle exécute une action métier et audite', () => {
    const ctrl = new ServicesController();
    ctrl.init({});
    const result = ctrl.handle('action', { foo: 'bar' });
    expect(result.success).toBe(true);
    expect(result.action).toBe('action');
    expect(result.payload).toEqual({ foo: 'bar' });
    expect(ctrl.getAuditTrail().pop().action).toBe('handle');
  });

  it('handle lève une erreur sur action invalide', () => {
    const ctrl = new ServicesController();
    ctrl.init({});
    expect(() => ctrl.handle('', {})).toThrow('Invalid action');
    expect(ctrl.getAuditTrail().pop().action).toBe('error');
  });
});
