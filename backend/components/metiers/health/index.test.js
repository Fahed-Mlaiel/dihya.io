// Tests unitaires & intégration – Health
import request from 'supertest';
import app from '../../../app.js';
describe('Health API', () => {
  it('GET /health/appointments – doit retourner les rendez-vous', async () => {
    const res = await request(app).get('/health/appointments');
    expect(res.statusCode).toBe(200);
    expect(res.body.appointments).toBeDefined();
  });
  it('POST /health/appointments – sécurité, validation', async () => {
    // ...mock JWT, RBAC, body, etc.
  });
});
