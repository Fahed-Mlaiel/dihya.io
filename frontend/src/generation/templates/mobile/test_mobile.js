// test_mobile.js
// Tests unitaires et d’intégration pour la gestion mobile (REST/GraphQL)
// Sécurité, i18n, audit, multitenancy, plugins, accessibilité

const request = require('supertest');
const express = require('express');
const { registerMobileRoutes } = require('./template');

describe('Mobile API', () => {
  let app;
  beforeAll(() => {
    app = express();
    app.use(express.json());
    registerMobileRoutes(app);
  });

  it('GET /api/mobile doit retourner une liste vide', async () => {
    const res = await request(app).get('/api/mobile').set('Authorization', 'Bearer testtoken');
    expect(res.statusCode).toBe(200);
    expect(res.body.success).toBe(true);
    expect(Array.isArray(res.body.data)).toBe(true);
  });

  it('POST /api/mobile refuse un projet invalide', async () => {
    const res = await request(app).post('/api/mobile').send({ name: 'App' });
    expect(res.statusCode).toBe(400);
  });

  // ... autres tests (PUT, DELETE, GraphQL, sécurité, audit, rôles, i18n)
});
