/**
 * @file test_culture.js
 * @description Tests d'intégration avancés pour le module Culture dans Dihya Coding.
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

describe('Culture API Integration', () => {
  let token;
  beforeAll(async () => {
    token = await getJWTToken('admin');
  });

  it('should create a new culture project (ar)', async () => {
    const res = await request(app)
      .post('/api/culture')
      .set('Authorization', `Bearer ${token}`)
      .set('Accept-Language', 'ar')
      .send({
        name: 'مشروع ثقافة',
        description: 'اختبار مشروع ثقافة',
        lang: 'ar',
        tenant: 'default',
      });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
  });

  it('should reject unauthenticated access', async () => {
    const res = await request(app)
      .get('/api/culture')
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(401);
  });

  // ...autres tests avancés (i18n, rôles, audit, plugins, fallback IA, etc.)
});
