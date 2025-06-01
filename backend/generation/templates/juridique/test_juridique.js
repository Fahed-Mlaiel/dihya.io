/**
 * Tests avancés Juridique – Dihya Coding
 * @coverage 100%
 */
const request = require('supertest');
const express = require('express');
const juridiqueRouter = require('./template');
const i18n = require('../../../../middlewares/i18n');

describe('Juridique API', () => {
  let app;
  beforeAll(() => {
    app = express();
    app.use(express.json());
    app.use(i18n);
    app.use('/api/juridique', juridiqueRouter);
  });

  it('crée un contrat (admin)', async () => {
    const res = await request(app)
      .post('/api/juridique/contrat')
      .set('Authorization', 'Bearer valid-admin-jwt')
      .send({ title: 'Test Contrat', content: 'Contenu', lang: 'fr' });
    expect(res.statusCode).toBe(201);
    expect(res.body.contrat).toBeDefined();
  });

  it('refuse sans JWT', async () => {
    const res = await request(app)
      .post('/api/juridique/contrat')
      .send({ title: 'Test Contrat', content: 'Contenu', lang: 'fr' });
    expect(res.statusCode).toBe(401);
  });

  it('liste les contrats (invité)', async () => {
    const res = await request(app)
      .get('/api/juridique/contrats')
      .set('Accept-Language', 'en');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body.contrats)).toBe(true);
  });
});
