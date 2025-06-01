// Tests unitaires & intégration – Mobile
import request from 'supertest';
import app from '../../../app.js';
describe('Mobile API', () => {
  it('GET /mobile/items – doit retourner les items', async () => {
    const res = await request(app).get('/mobile/items');
    expect(res.statusCode).toBe(200);
    expect(res.body.items).toBeDefined();
  });
  it('POST /mobile/items – sécurité, validation', async () => {
    // ...mock JWT, RBAC, body, etc.
  });
});
