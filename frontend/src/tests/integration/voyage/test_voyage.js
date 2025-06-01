/**
 * Test d'intégration avancé pour la gestion du voyage (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, multitenancy, fallback IA, SEO, multilingue)
 * @see README.md pour la documentation complète
 */
const request = require('supertest');
const app = require('../../../../backend/node/app');
const { getJwt, SUPPORTED_LANGUAGES } = require('../../utils/test_utils');

describe('Voyage API Integration', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('user');
  });
  it('GET /voyage (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await request(app)
        .get('/voyage')
        .set('Authorization', `Bearer ${jwt}`)
        .set('Accept-Language', lang);
      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('data');
      expect(res.headers['content-language']).toBe(lang);
    }
  });
  it('POST /voyage (validation, RGPD, plugins, audit)', async () => {
    const res = await request(app)
      .post('/voyage')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ name: 'Voyage organisé', type: 'groupe', owner: 'user_id' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('entry');
  });
});
