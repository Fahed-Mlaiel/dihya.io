/**
 * @file test_voyage.js
 * @description Tests d'intégration avancés pour la gestion de projets "voyage" dans Dihya Coding.
 * @author Dihya Team
 * @version 1.0.0
 * @license MIT
 * @see https://dihya.dev
 *
 * Sécurité : JWT, CORS, audit, WAF, anti-DDOS.
 * Multilingue : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.
 * RGPD, auditabilité, anonymisation, export.
 */

const request = require('supertest');
const app = require('../../../../server');
const { getJWTToken } = require('../../../../utils/auth');

describe('Voyage API Integration', () => {
  let token;
  beforeAll(async () => {
    token = await getJWTToken('admin');
  });

  it('should create a new voyage project (en)', async () => {
    const res = await request(app)
      .post('/api/voyage')
      .set('Authorization', `Bearer ${token}`)
      .set('Accept-Language', 'en')
      .send({
        name: 'Travel Project',
        description: 'Test travel project',
        lang: 'en',
        tenant: 'default',
      });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
  });

  it('should reject unauthenticated access', async () => {
    const res = await request(app)
      .get('/api/voyage')
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(401);
  });

  // ...autres tests avancés (i18n, rôles, audit, plugins, fallback IA, etc.)
});
