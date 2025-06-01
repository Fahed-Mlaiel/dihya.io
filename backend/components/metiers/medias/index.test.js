// Tests unitaires & intégration – Medias
import request from 'supertest';
import app from '../../../app.js';
describe('Medias API', () => {
  it('GET /medias/items – doit retourner les médias', async () => {
    const res = await request(app).get('/medias/items');
    expect(res.statusCode).toBe(200);
    expect(res.body.items).toBeDefined();
  });
  it('POST /medias/items – sécurité, validation', async () => {
    // ...mock JWT, RBAC, body, etc.
  });
});
