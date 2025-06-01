// Tests unitaires & intégration – Environnement
import request from 'supertest';
import app from '../../../app.js';
describe('Environnement API', () => {
  it('GET /environnement/data – doit retourner les données', async () => {
    const res = await request(app).get('/environnement/data');
    expect(res.statusCode).toBe(200);
    expect(res.body.data).toBeDefined();
  });
  it('POST /environnement/alerts – sécurité, validation', async () => {
    // ...mock JWT, RBAC, body, etc.
  });
});
