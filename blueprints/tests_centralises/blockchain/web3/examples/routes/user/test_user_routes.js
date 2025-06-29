const ServicesIndex = require('../../../../../../blockchain/services/index');
describe('ServicesIndex (user routes)', () => {
  it('gère la route GET /user/profile', () => {
    const service = new ServicesIndex({});
    const result = service.execute({ route: '/user/profile', method: 'GET', userId: 'user1' });
    expect(result).toBeDefined();
    expect(result.userId).toBe('user1');
  });
  it('gère la route POST /user/register', () => {
    const service = new ServicesIndex({});
    const result = service.execute({ route: '/user/register', method: 'POST', data: { login: 'user2', pass: 'pass2' } });
    expect(result).toBeDefined();
    expect(result.status).toBe('registered');
  });
  it('doit exécuter la logique métier sans erreur', () => {
    const service = new ServicesIndex({});
    expect(() => service.execute({ test: true })).not.toThrow();
  });
});
