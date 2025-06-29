// Test ultra avancé pour le blueprint backendApi (Express)
const request = require('supertest');
const backendApi = require('../../../../blueprints/api/generators/backendApi');

describe('backendApi Express', () => {
  const app = eval(backendApi({ metier: 'Inventaire', dependances: {}, plugins: {}, rgpd: true }));
  it('GET /api/Inventaire doit répondre 200', async () => {
    const res = await request(app).get('/api/Inventaire');
    expect(res.statusCode).toBe(200);
    expect(res.body.message).toMatch(/opérationnelle/);
  });
});
