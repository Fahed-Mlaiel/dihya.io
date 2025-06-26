// Tests avancés pour la sécurité threed
const { checkAccess, auditLog, validateToken } = require('../../api/security');
describe('Sécurité threed', () => {
  it('doit refuser l’accès sans token', () => {
    expect(() => checkAccess(null)).toThrow();
  });
  it('doit valider un token JWT conforme', () => {
    const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...';
    expect(validateToken(token)).toBe(true);
  });
  it('doit enregistrer un audit log', () => {
    const result = auditLog({ action: 'login', user: 'admin' });
    expect(result).toHaveProperty('timestamp');
  });
});
