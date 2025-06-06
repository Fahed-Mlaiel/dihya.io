// core_utils.test.js – Tests unitaires ultra avancés pour core_utils.js
const core = require('./core_utils');

describe('core_utils – Génération d’ID', () => {
  it('génère un ID unique avec préfixe', () => {
    const id = core.generateId('asset');
    expect(id.startsWith('asset-')).toBe(true);
    expect(id.length).toBeGreaterThan(10);
  });
});

describe('core_utils – deepClone', () => {
  it('clone profondément un objet', () => {
    const obj = { a: 1, b: { c: 2 } };
    const clone = core.deepClone(obj);
    expect(clone).toEqual(obj);
    expect(clone).not.toBe(obj);
    expect(clone.b).not.toBe(obj.b);
  });
});

describe('core_utils – isValidEmail', () => {
  it('valide les emails corrects', () => {
    expect(core.isValidEmail('test@dihya.io')).toBe(true);
  });
  it('rejette les emails invalides', () => {
    expect(core.isValidEmail('not-an-email')).toBe(false);
  });
});

describe('core_utils – auditLog', () => {
  it('génère un log d’audit conforme', () => {
    const log = core.auditLog('LOGIN', 'user-001', { ip: '127.0.0.1' });
    expect(log).toHaveProperty('id');
    expect(log).toHaveProperty('action', 'LOGIN');
    expect(log).toHaveProperty('user', 'user-001');
    expect(log).toHaveProperty('meta');
    expect(log).toHaveProperty('timestamp');
  });
});
