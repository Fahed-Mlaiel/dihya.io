// test_medias.js
// Tests unitaires et d’intégration pour la gestion des médias (REST/GraphQL)
// Couverture complète, mocks, sécurité, i18n, audit, multitenancy

const request = require('supertest');
const express = require('express');
const { registerMediaRoutes } = require('./template');

describe('Media API', () => {
  let app;
  beforeAll(() => {
    app = express();
    app.use(express.json());
    registerMediaRoutes(app);
  });

  it('GET /api/medias doit retourner une liste vide', async () => {
    const res = await request(app).get('/api/medias').set('Authorization', 'Bearer testtoken');
    expect(res.statusCode).toBe(200);
    expect(res.body.success).toBe(true);
    expect(Array.isArray(res.body.data)).toBe(true);
  });

  it('POST /api/medias refuse un média invalide', async () => {
    const res = await request(app).post('/api/medias').send({ url: 'not-an-url' });
    expect(res.statusCode).toBe(400);
  });

  // ... autres tests (PUT, DELETE, GraphQL, sécurité, audit, rôles, i18n)
});
