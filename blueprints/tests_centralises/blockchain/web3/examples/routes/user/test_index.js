const ServicesIndex = require('../../../../../../blockchain/services/index');
describe('ServicesIndex (user)', () => {
  it('exécute la logique métier utilisateur', () => {
    const service = new ServicesIndex({ user: 'user1' });
    const result = service.execute({ action: 'login', credentials: { login: 'user1', pass: 'pass' } });
    expect(result).toBeDefined();
  });
  it('gère l’inscription utilisateur', () => {
    const service = new ServicesIndex({});
    const result = service.execute({ action: 'register', data: { login: 'user2', pass: 'pass2' } });
    expect(result).toBeDefined();
  });
});
