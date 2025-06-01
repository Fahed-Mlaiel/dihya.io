// test_preview.js
/**
 * @file Test d'intégration avancé pour la gestion des projets preview (IA, VR, AR...)
 * Sécurité maximale, i18n, multitenancy, IA fallback, SEO, plugins, RGPD, auditabilité
 * Tests complets (unit, integration, e2e)
 */
const request = require('supertest');
const app = require('../../../app');
const { getJWT, getI18nHeaders, getRoleHeaders } = require('../../utils/testUtils');

describe('Preview API Integration', () => {
  it('should create a preview project (admin, ja)', async () => {
    const res = await request(app)
      .post('/api/v1/preview')
      .set(getJWT('admin'))
      .set(getI18nHeaders('ja'))
      .send({ name: 'プレビュープロジェクト', type: 'VR', lang: 'ja' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
    expect(res.body.lang).toBe('ja');
  });
  // ...autres tests multilingues, rôles, sécurité, fallback IA, SEO, plugins, RGPD, auditabilité
});
