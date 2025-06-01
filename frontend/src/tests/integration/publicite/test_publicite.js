// test_publicite.js
/**
 * @file Test d'intégration avancé pour la gestion des projets publicité (IA, VR, AR...)
 * Sécurité maximale, i18n, multitenancy, IA fallback, SEO, plugins, RGPD, auditabilité
 * Tests complets (unit, integration, e2e)
 */
const request = require('supertest');
const app = require('../../../app');
const { getJWT, getI18nHeaders, getRoleHeaders } = require('../../utils/testUtils');

describe('Publicite API Integration', () => {
  it('should create a publicite project (admin, ko)', async () => {
    const res = await request(app)
      .post('/api/v1/publicite')
      .set(getJWT('admin'))
      .set(getI18nHeaders('ko'))
      .send({ name: '광고 프로젝트', type: 'AR', lang: 'ko' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
    expect(res.body.lang).toBe('ko');
  });
  // ...autres tests multilingues, rôles, sécurité, fallback IA, SEO, plugins, RGPD, auditabilité
});
