// __init__.test.js – Test d'import global du module core (JS)
const core = require('./__init__');

describe('__init__ (core)', () => {
  it('importe tous les utilitaires core', () => {
    expect(core.generateId).toBeDefined();
    expect(core.deepClone).toBeDefined();
    expect(core.isValidEmail).toBeDefined();
    expect(core.auditLog).toBeDefined();
  });
});
