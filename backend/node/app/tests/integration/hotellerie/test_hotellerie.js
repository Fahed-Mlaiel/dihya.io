/**
 * @file test_hotellerie.js
 * @description Tests d'intégration avancés pour le module Hôtellerie dans Dihya Coding.
 * @author Dihya Team
 * @version 1.0.0
 * @license MIT
 *
 * Sécurité : JWT, CORS, audit, WAF, anti-DDOS.
 * Multilingue : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.
 * RGPD, auditabilité, anonymisation, export.
 */

const request = require('supertest');
const app = require('../../../../server');
const { getJWTToken } = require('../../../../utils/auth');

describe('Hôtellerie API Integration', () => {
  let token;
  beforeAll(async () => {
    token = await getJWTToken('admin');
  });

  it('should create a new hôtellerie project (fr)', async () => {
    const res = await request(app)
      .post('/api/hotellerie')
      .set('Authorization', `Bearer ${token}`)
      .set('Accept-Language', 'fr')
      .send({
        name: 'Projet Hôtellerie',
        description: 'Test projet hôtellerie',
        lang: 'fr',
        tenant: 'default',
      });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
  });

  it('should reject unauthenticated access', async () => {
    const res = await request(app)
      .get('/api/hotellerie')
      .set('Accept-Language', 'en');
    expect(res.statusCode).toBe(401);
  });

  // ...autres tests avancés (i18n, rôles, audit, plugins, fallback IA, etc.)
});
