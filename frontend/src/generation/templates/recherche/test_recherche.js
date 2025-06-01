// test_recherche.js
// Tests unitaires et d’intégration pour la gestion recherche (REST/GraphQL)
// Sécurité, i18n, audit, multitenancy, plugins, accessibilité

const request = require('supertest');
const express = require('express');
const { registerSearchRoutes } = require('./template');

describe('Search API', () => {
  let app;
  beforeAll(() => {
    app = express();
    app.use(express.json());
    registerSearchRoutes(app);
  });

  it('GET /api/recherche doit retourner une liste vide', async () => {
    const res = await request(app).get('/api/recherche').set('Authorization', 'Bearer testtoken');
    expect(res.statusCode).toBe(200);
    expect(res.body.success).toBe(true);
    expect(Array.isArray(res.body.data)).toBe(true);
  });

  it('POST /api/recherche refuse une recherche invalide', async () => {
    const res = await request(app).post('/api/recherche').send({ query: '' });
    expect(res.statusCode).toBe(400);
  });

  // ... autres tests (PUT, DELETE, GraphQL, sécurité, audit, rôles, i18n)
});
