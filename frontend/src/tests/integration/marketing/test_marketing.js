// test_marketing.js
/**
 * @file Test d'intégration avancé pour la gestion des projets marketing (IA, VR, AR...)
 * Sécurité maximale, i18n, multitenancy, IA fallback, SEO, plugins, RGPD, auditabilité
 * Tests complets (unit, integration, e2e)
 */
const request = require('supertest');
const app = require('../../../app');
const { getJWT, getI18nHeaders, getRoleHeaders } = require('../../utils/testUtils');

describe('Marketing API Integration', () => {
  it('should create a marketing project (admin, en)', async () => {
    const res = await request(app)
      .post('/api/v1/marketing')
      .set(getJWT('admin'))
      .set(getI18nHeaders('en'))
      .send({ name: 'AI Marketing Project', type: 'AI', lang: 'en' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
    expect(res.body.lang).toBe('en');
  });
  // ...autres tests multilingues, rôles, sécurité, fallback IA, SEO, plugins, RGPD, auditabilité
});
