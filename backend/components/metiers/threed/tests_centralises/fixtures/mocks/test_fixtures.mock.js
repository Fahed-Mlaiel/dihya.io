// test_fixtures.mock.js – Tests ultra avancés pour les mocks fixtures (JS)
const { mockRequest, mockResponse } = require('./fixtures.mock');

test('mockRequest retourne une requête mockée', () => {
  const req = mockRequest({ foo: 'bar' });
  expect(req.headers['x-test']).toBe('true');
  expect(req.user.id).toBe('mock-user');
  expect(req.user.role).toBe('test');
  expect(req.body.foo).toBe('bar');
});

test('mockResponse retourne une réponse mockée', () => {
  const res = mockResponse();
  expect(typeof res.status).toBe('function');
  expect(typeof res.json).toBe('function');
  expect(res.status()).toBe(res);
  expect(res.json()).toBe(res);
});
