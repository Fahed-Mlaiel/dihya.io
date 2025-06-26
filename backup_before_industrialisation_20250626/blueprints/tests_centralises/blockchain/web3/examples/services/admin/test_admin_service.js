const ServicesIndex = require('../../../../../../blockchain/services/index');
describe('ServicesIndex (admin)', () => {
  it('crée un nouvel administrateur', () => {
    const service = new ServicesIndex({});
    const result = service.execute({ action: 'createAdmin', data: { login: 'admin1', pass: 'adminpass' } });
    expect(result).toBeDefined();
    expect(result.role).toBe('admin');
  });
  it('révoque un administrateur', () => {
    const service = new ServicesIndex({});
    const result = service.execute({ action: 'revokeAdmin', adminId: 'admin1' });
    expect(result).toBeDefined();
    expect(result.status).toBe('revoked');
  });
});
