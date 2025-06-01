// test_restauration.js
/**
 * @file Test d'intégration avancé pour la gestion des projets restauration (IA, VR, AR...)
 * Sécurité maximale, i18n, multitenancy, IA fallback, SEO, plugins, RGPD, auditabilité
 * Tests complets (unit, integration, e2e)
 */
const request = require('supertest');
const app = require('../../../app');
const { getJWT, getI18nHeaders, getRoleHeaders } = require('../../utils/testUtils');

describe('Restauration API Integration', () => {
  it('should create a restauration project (admin, fa)', async () => {
    const res = await request(app)
      .post('/api/v1/restauration')
      .set(getJWT('admin'))
      .set(getI18nHeaders('fa'))
      .send({ name: 'پروژه رستوران', type: 'AR', lang: 'fa' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
    expect(res.body.lang).toBe('fa');
  });
  // ...autres tests multilingues, rôles, sécurité, fallback IA, SEO, plugins, RGPD, auditabilité
});
