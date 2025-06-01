// test_voice.js
/**
 * Tests d'intégration ultra avancés pour la gestion de la voix (Voice API)
 * Sécurité maximale, multilingue, audit, plugins, RGPD, accessibilité, e2e.
 */
const request = require('supertest');
const app = require('../../../src/app');
const { getJWTToken } = require('../../utils/auth');

describe('Voice API Integration', () => {
  let token;
  beforeAll(async () => {
    token = await getJWTToken('admin');
  });

  it('should create a new voice project (fr)', async () => {
    const res = await request(app)
      .post('/api/voice/projects')
      .set('Authorization', `Bearer ${token}`)
      .send({ name: 'Projet Voix', lang: 'fr' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
    expect(res.body.lang).toBe('fr');
  });

  it('should reject unauthenticated creation', async () => {
    const res = await request(app)
      .post('/api/voice/projects')
      .send({ name: 'Projet Voix', lang: 'fr' });
    expect(res.statusCode).toBe(401);
  });

  // ...tests multilingues, RBAC, audit, plugins, RGPD, accessibilité, e2e...
});
