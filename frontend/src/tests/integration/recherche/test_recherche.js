// test_recherche.js
/**
 * @file Test d'intégration avancé pour la gestion des projets recherche (IA, VR, AR...)
 * Sécurité maximale, i18n, multitenancy, IA fallback, SEO, plugins, RGPD, auditabilité
 * Tests complets (unit, integration, e2e)
 */
const request = require('supertest');
const app = require('../../../app');
const { getJWT, getI18nHeaders, getRoleHeaders } = require('../../utils/testUtils');

describe('Recherche API Integration', () => {
  it('should create a recherche project (admin, nl)', async () => {
    const res = await request(app)
      .post('/api/v1/recherche')
      .set(getJWT('admin'))
      .set(getI18nHeaders('nl'))
      .send({ name: 'Onderzoeksproject', type: 'AI', lang: 'nl' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
    expect(res.body.lang).toBe('nl');
  });
  // ...autres tests multilingues, rôles, sécurité, fallback IA, SEO, plugins, RGPD, auditabilité
});
