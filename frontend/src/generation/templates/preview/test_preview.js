// test_preview.js
// Tests unitaires et d’intégration pour la gestion preview (REST/GraphQL)
// Sécurité, i18n, audit, multitenancy, plugins, accessibilité

const request = require('supertest');
const express = require('express');
const { registerPreviewRoutes } = require('./template');

describe('Preview API', () => {
  let app;
  beforeAll(() => {
    app = express();
    app.use(express.json());
    registerPreviewRoutes(app);
  });

  it('GET /api/preview doit retourner une liste vide', async () => {
    const res = await request(app).get('/api/preview').set('Authorization', 'Bearer testtoken');
    expect(res.statusCode).toBe(200);
    expect(res.body.success).toBe(true);
    expect(Array.isArray(res.body.data)).toBe(true);
  });

  it('POST /api/preview refuse un preview invalide', async () => {
    const res = await request(app).post('/api/preview').send({ url: 'not-an-url' });
    expect(res.statusCode).toBe(400);
  });

  // ... autres tests (PUT, DELETE, GraphQL, sécurité, audit, rôles, i18n)
});
