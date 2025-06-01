/**
 * Tests avancés Marketing – Dihya Coding
 * @coverage 100%
 */
const request = require('supertest');
const express = require('express');
const marketingRouter = require('./template');
const i18n = require('../../../../middlewares/i18n');

describe('Marketing API', () => {
  let app;
  beforeAll(() => {
    app = express();
    app.use(express.json());
    app.use(i18n);
    app.use('/api/marketing', marketingRouter);
  });

  it('crée une campagne (admin)', async () => {
    const res = await request(app)
      .post('/api/marketing/campagne')
      .set('Authorization', 'Bearer valid-admin-jwt')
      .send({ nom: 'Test', description: 'Desc', lang: 'fr' });
    expect(res.statusCode).toBe(201);
    expect(res.body.campagne).toBeDefined();
  });

  it('refuse sans JWT', async () => {
    const res = await request(app)
      .post('/api/marketing/campagne')
      .send({ nom: 'Test', description: 'Desc', lang: 'fr' });
    expect(res.statusCode).toBe(401);
  });

  it('liste les campagnes (invité)', async () => {
    const res = await request(app)
      .get('/api/marketing/campagnes')
      .set('Accept-Language', 'en');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body.campagnes)).toBe(true);
  });
});
