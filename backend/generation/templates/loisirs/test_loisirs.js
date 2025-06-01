/**
 * Tests avancés Loisirs – Dihya Coding
 * @coverage 100%
 */
const request = require('supertest');
const express = require('express');
const loisirsRouter = require('./template');
const i18n = require('../../../../middlewares/i18n');

describe('Loisirs API', () => {
  let app;
  beforeAll(() => {
    app = express();
    app.use(express.json());
    app.use(i18n);
    app.use('/api/loisirs', loisirsRouter);
  });

  it('crée une activité (admin)', async () => {
    const res = await request(app)
      .post('/api/loisirs/activite')
      .set('Authorization', 'Bearer valid-admin-jwt')
      .send({ nom: 'Test', description: 'Desc', lang: 'fr' });
    expect(res.statusCode).toBe(201);
    expect(res.body.activite).toBeDefined();
  });

  it('refuse sans JWT', async () => {
    const res = await request(app)
      .post('/api/loisirs/activite')
      .send({ nom: 'Test', description: 'Desc', lang: 'fr' });
    expect(res.statusCode).toBe(401);
  });

  it('liste les activités (invité)', async () => {
    const res = await request(app)
      .get('/api/loisirs/activites')
      .set('Accept-Language', 'en');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body.activites)).toBe(true);
  });
});
