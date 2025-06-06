// test_api.js – Tests avancés de l'API Environnement (Node.js/Jest)
const request = require('supertest');
const app = require('../../index'); // Adapter selon l'entrée réelle de l'app

describe('API Environnement', () => {
  it('GET /environnements doit retourner la liste', async () => {
    const res = await request(app).get('/environnements');
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('environnements');
    expect(Array.isArray(res.body.environnements)).toBe(true);
  });

  it('POST /environnements crée une entité', async () => {
    const data = { nom: 'Test JS', description: 'desc', type: 'zone' };
    const res = await request(app).post('/environnements').send(data);
    expect(res.statusCode).toBe(201);
    expect(res.body.nom).toBe('Test JS');
  });
});
