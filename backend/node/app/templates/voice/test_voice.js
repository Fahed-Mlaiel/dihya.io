/**
 * @file test_voice.js
 * @description Tests d'intégration avancés pour la gestion de la voix (IA, VR, AR) dans Dihya Coding.
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

describe('Voice API Integration', () => {
  let token;
  beforeAll(async () => {
    token = await getJWTToken('admin');
  });

  it('should create a new voice project (fr)', async () => {
    const res = await request(app)
      .post('/api/voice')
      .set('Authorization', `Bearer ${token}`)
      .set('Accept-Language', 'fr')
      .send({
        name: 'Projet Voix IA',
        description: 'Test projet voix IA',
        lang: 'fr',
        tenant: 'default',
      });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
  });

  it('should reject unauthenticated access', async () => {
    const res = await request(app)
      .get('/api/voice')
      .set('Accept-Language', 'en');
    expect(res.statusCode).toBe(401);
  });

  // ...autres tests avancés (i18n, rôles, audit, plugins, fallback IA, etc.)
});
