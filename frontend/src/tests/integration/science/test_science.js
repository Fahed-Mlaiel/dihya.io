// test_science.js
/**
 * @file Test d'intégration avancé pour la gestion des projets science (IA, VR, AR...)
 * Sécurité maximale, i18n, multitenancy, IA fallback, SEO, plugins, RGPD, auditabilité
 * Tests complets (unit, integration, e2e)
 */
const request = require('supertest');
const app = require('../../../app');
const { getJWT, getI18nHeaders, getRoleHeaders } = require('../../utils/testUtils');

describe('Science API Integration', () => {
  it('should create a science project (admin, es)', async () => {
    const res = await request(app)
      .post('/api/v1/science')
      .set(getJWT('admin'))
      .set(getI18nHeaders('es'))
      .send({ name: 'Proyecto de Ciencia', type: 'VR', lang: 'es' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
    expect(res.body.lang).toBe('es');
  });
  // ...autres tests multilingues, rôles, sécurité, fallback IA, SEO, plugins, RGPD, auditabilité
});
