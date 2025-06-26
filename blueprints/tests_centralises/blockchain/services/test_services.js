const ServicesIndex = require('../../../../blockchain/services/index');

describe('ServicesIndex', () => {
  it('instancie et exécute la logique métier principale', () => {
    const service = new ServicesIndex({ env: 'test' });
    const result = service.execute({ foo: 'bar' });
    expect(result).toEqual({ foo: 'bar' });
  });
});
