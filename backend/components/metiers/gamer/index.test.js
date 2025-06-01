// Tests unitaires & intégration – Gamer
import request from 'supertest';
import app from '../../../app.js';
describe('Gamer API', () => {
  it('GET /gamer/tournaments – doit retourner les tournois', async () => {
    const res = await request(app).get('/gamer/tournaments');
    expect(res.statusCode).toBe(200);
    expect(res.body.tournaments).toBeDefined();
  });
  it('POST /gamer/tournaments – sécurité, validation', async () => {
    // ...mock JWT, RBAC, body, etc.
  });
});
