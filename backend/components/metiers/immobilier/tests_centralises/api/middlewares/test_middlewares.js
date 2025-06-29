// test_middlewares.js – Test ultra avancé des middlewares API Immobilier (centralisé)

const { sampleMiddlewareUltra } = require('../../../api/samples/middlewares');

describe('Middlewares API Immobilier', () => {
  it('doit exécuter le middleware ultra avancé', () => {
    const request = { user: { id: 1 }, headers: { 'x-test': 'true' } };
    const result = sampleMiddlewareUltra(request);
    expect(result.request).toEqual(request);
    expect(result.middleware).toBe('applied');
  });
});
