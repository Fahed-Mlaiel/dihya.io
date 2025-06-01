// test_logistique.js – Tests unitaires et intégration pour le module logistique

const request = require('supertest');
const app = require('../../app');

describe('Logistique API', () => {
  it('GET /logistique/info – doit retourner un message multilingue et sécurisé', async () => {
    const res = await request(app)
      .get('/logistique/info')
      .set('Authorization', 'Bearer FAKE_JWT')
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('message');
    expect(res.body.message).toMatch(/Bienvenue|Welcome|مرحبًا/);
  });

  it('POST /logistique/create – doit créer une ressource logistique', async () => {
    const res = await request(app)
      .post('/logistique/create')
      .set('Authorization', 'Bearer FAKE_JWT')
      .send({ name: 'Test', type: 'Transport' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('message');
    expect(res.body.message).toMatch(/créée|created/);
  });
});
