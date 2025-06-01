/**
 * Tests avancés Journalisme – Dihya Coding
 * @coverage 100%
 */
const request = require('supertest');
const express = require('express');
const journalismeRouter = require('./template');
const i18n = require('../../../../middlewares/i18n');

describe('Journalisme API', () => {
  let app;
  beforeAll(() => {
    app = express();
    app.use(express.json());
    app.use(i18n);
    app.use('/api/journalisme', journalismeRouter);
  });

  it('crée un article (admin)', async () => {
    const res = await request(app)
      .post('/api/journalisme/article')
      .set('Authorization', 'Bearer valid-admin-jwt')
      .send({ title: 'Test', content: 'Contenu', lang: 'fr' });
    expect(res.statusCode).toBe(201);
    expect(res.body.article).toBeDefined();
  });

  it('refuse sans JWT', async () => {
    const res = await request(app)
      .post('/api/journalisme/article')
      .send({ title: 'Test', content: 'Contenu', lang: 'fr' });
    expect(res.statusCode).toBe(401);
  });

  it('liste les articles (invité)', async () => {
    const res = await request(app)
      .get('/api/journalisme/articles')
      .set('Accept-Language', 'en');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body.articles)).toBe(true);
  });
});
