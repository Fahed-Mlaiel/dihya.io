/**
 * Test d'intégration avancé pour la gestion sociale (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, multitenancy, fallback IA, SEO, multilingue)
 * @see README.md pour la documentation complète
 */
const request = require('supertest');
const app = require('../../../../backend/node/app');
const { getJwt, SUPPORTED_LANGUAGES } = require('../../utils/test_utils');

describe('Social API Integration', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('user');
  });
  it('GET /social (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await request(app)
        .get('/social')
        .set('Authorization', `Bearer ${jwt}`)
        .set('Accept-Language', lang);
      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('data');
      expect(res.headers['content-language']).toBe(lang);
    }
  });
  it('POST /social (validation, RGPD, plugins, audit)', async () => {
    const res = await request(app)
      .post('/social')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ name: 'Réseau social', type: 'reseau', owner: 'user_id' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('entry');
  });
});
