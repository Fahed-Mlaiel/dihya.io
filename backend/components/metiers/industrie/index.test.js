// Tests unitaires & intégration – Industrie
import request from 'supertest';
import app from '../../../app.js';
describe('Industrie API', () => {
  it('GET /industrie/factories – doit retourner les usines', async () => {
    const res = await request(app).get('/industrie/factories');
    expect(res.statusCode).toBe(200);
    expect(res.body.factories).toBeDefined();
  });
  it('POST /industrie/factories – sécurité, validation', async () => {
    // ...mock JWT, RBAC, body, etc.
  });
});
