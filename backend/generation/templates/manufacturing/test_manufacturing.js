/**
 * Tests avancés Manufacturing – Dihya Coding
 * @coverage 100%
 */
const request = require('supertest');
const express = require('express');
const manufacturingRouter = require('./template');
const i18n = require('../../../../middlewares/i18n');

describe('Manufacturing API', () => {
  let app;
  beforeAll(() => {
    app = express();
    app.use(express.json());
    app.use(i18n);
    app.use('/api/manufacturing', manufacturingRouter);
  });

  it('crée un ordre de production (admin)', async () => {
    const res = await request(app)
      .post('/api/manufacturing/production')
      .set('Authorization', 'Bearer valid-admin-jwt')
      .send({ ref: 'Test', quantite: 100, lang: 'fr' });
    expect(res.statusCode).toBe(201);
    expect(res.body.production).toBeDefined();
  });

  it('refuse sans JWT', async () => {
    const res = await request(app)
      .post('/api/manufacturing/production')
      .send({ ref: 'Test', quantite: 100, lang: 'fr' });
    expect(res.statusCode).toBe(401);
  });

  it('liste les ordres (invité)', async () => {
    const res = await request(app)
      .get('/api/manufacturing/productions')
      .set('Accept-Language', 'en');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body.productions)).toBe(true);
  });
});
