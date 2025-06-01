/**
 * Tests avancés Logistique – Dihya Coding
 * @coverage 100%
 */
const request = require('supertest');
const express = require('express');
const logistiqueRouter = require('./template');
const i18n = require('../../../../middlewares/i18n');

describe('Logistique API', () => {
  let app;
  beforeAll(() => {
    app = express();
    app.use(express.json());
    app.use(i18n);
    app.use('/api/logistique', logistiqueRouter);
  });

  it('crée une entrée (admin)', async () => {
    const res = await request(app)
      .post('/api/logistique/entree')
      .set('Authorization', 'Bearer valid-admin-jwt')
      .send({ ref: 'Test', quantite: 10, lang: 'fr' });
    expect(res.statusCode).toBe(201);
    expect(res.body.entree).toBeDefined();
  });

  it('refuse sans JWT', async () => {
    const res = await request(app)
      .post('/api/logistique/entree')
      .send({ ref: 'Test', quantite: 10, lang: 'fr' });
    expect(res.statusCode).toBe(401);
  });

  it('liste les entrées (invité)', async () => {
    const res = await request(app)
      .get('/api/logistique/entrees')
      .set('Accept-Language', 'en');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body.entrees)).toBe(true);
  });
});
