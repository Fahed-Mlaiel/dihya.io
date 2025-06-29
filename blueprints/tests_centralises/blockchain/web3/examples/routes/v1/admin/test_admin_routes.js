const ServicesIndex = require('../../../../../../blockchain/services/index');

describe('ServicesIndex (admin routes)', () => {
  it('gère la route GET /admin/list', () => {
    const service = new ServicesIndex({});
    const result = service.execute({ route: '/admin/list', method: 'GET' });
    expect(result).toBeDefined();
    expect(Array.isArray(result.admins)).toBe(true);
  });
  it('gère la route POST /admin/create', () => {
    const service = new ServicesIndex({});
    const result = service.execute({ route: '/admin/create', method: 'POST', data: { login: 'admin2', pass: 'pass2' } });
    expect(result).toBeDefined();
    expect(result.status).toBe('created');
  });
});
