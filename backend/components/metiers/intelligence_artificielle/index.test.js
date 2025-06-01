// Tests unitaires & intégration – Intelligence Artificielle
import request from 'supertest';
import app from '../../../app.js';
describe('Intelligence Artificielle API', () => {
  it('GET /intelligence_artificielle/models – doit retourner les modèles', async () => {
    const res = await request(app).get('/intelligence_artificielle/models');
    expect(res.statusCode).toBe(200);
    expect(res.body.models).toBeDefined();
  });
  it('POST /intelligence_artificielle/models – sécurité, validation', async () => {
    // ...mock JWT, RBAC, body, etc.
  });
});
