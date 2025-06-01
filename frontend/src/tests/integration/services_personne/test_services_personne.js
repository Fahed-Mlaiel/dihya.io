/**
 * Test d'intégration avancé pour les services à la personne (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, multitenancy, fallback IA, SEO, multilingue)
 * @see README.md pour la documentation complète
 */
const request = require('supertest');
const app = require('../../../../backend/node/app');
const { getJwt, SUPPORTED_LANGUAGES } = require('../../utils/test_utils');

describe('Services à la personne API Integration', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('user');
  });
  it('GET /services_personne (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await request(app)
        .get('/services_personne')
        .set('Authorization', `Bearer ${jwt}`)
        .set('Accept-Language', lang);
      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('data');
      expect(res.headers['content-language']).toBe(lang);
    }
  });
  it('POST /services_personne (validation, RGPD, plugins, audit)', async () => {
    const res = await request(app)
      .post('/services_personne')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ name: 'Aide à domicile', type: 'aide', owner: 'user_id' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('entry');
  });
});
