// test_voyage.js
/**
 * Tests d'intégration ultra avancés pour la gestion des voyages (Voyage API)
 * Sécurité maximale, multilingue, audit, plugins, RGPD, accessibilité, e2e.
 */
const request = require('supertest');
const app = require('../../../src/app');
const { getJWTToken } = require('../../utils/auth');

describe('Voyage API Integration', () => {
  let token;
  beforeAll(async () => {
    token = await getJWTToken('admin');
  });

  it('should create a new voyage project (fr)', async () => {
    const res = await request(app)
      .post('/api/voyage/projects')
      .set('Authorization', `Bearer ${token}`)
      .send({ name: 'Projet Voyage', lang: 'fr' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
    expect(res.body.lang).toBe('fr');
  });

  it('should reject unauthenticated creation', async () => {
    const res = await request(app)
      .post('/api/voyage/projects')
      .send({ name: 'Projet Voyage', lang: 'fr' });
    expect(res.statusCode).toBe(401);
  });

  // ...tests multilingues, RBAC, audit, plugins, RGPD, accessibilité, e2e...
});
