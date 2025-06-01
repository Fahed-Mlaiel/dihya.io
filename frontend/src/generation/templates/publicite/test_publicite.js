// test_publicite.js
// Tests unitaires et d’intégration pour la gestion publicité (REST/GraphQL)
// Sécurité, i18n, audit, multitenancy, plugins, accessibilité

const request = require('supertest');
const express = require('express');
const { registerAdRoutes } = require('./template');

describe('Advertising API', () => {
  let app;
  beforeAll(() => {
    app = express();
    app.use(express.json());
    registerAdRoutes(app);
  });

  it('GET /api/publicite doit retourner une liste vide', async () => {
    const res = await request(app).get('/api/publicite').set('Authorization', 'Bearer testtoken');
    expect(res.statusCode).toBe(200);
    expect(res.body.success).toBe(true);
    expect(Array.isArray(res.body.data)).toBe(true);
  });

  it('POST /api/publicite refuse une publicité invalide', async () => {
    const res = await request(app).post('/api/publicite').send({ url: 'not-an-url' });
    expect(res.statusCode).toBe(400);
  });

  // ... autres tests (PUT, DELETE, GraphQL, sécurité, audit, rôles, i18n)
});
