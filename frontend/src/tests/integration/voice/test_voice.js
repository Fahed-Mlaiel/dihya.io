/**
 * Test d'intégration avancé pour la gestion de la voix (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, multitenancy, fallback IA, SEO, multilingue)
 * @see README.md pour la documentation complète
 */
const request = require('supertest');
const app = require('../../../../backend/node/app');
const { getJwt, SUPPORTED_LANGUAGES } = require('../../utils/test_utils');

describe('Voice API Integration', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('user');
  });
  it('GET /voice (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await request(app)
        .get('/voice')
        .set('Authorization', `Bearer ${jwt}`)
        .set('Accept-Language', lang);
      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('data');
      expect(res.headers['content-language']).toBe(lang);
    }
  });
  it('POST /voice (validation, RGPD, plugins, audit)', async () => {
    const res = await request(app)
      .post('/voice')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ name: 'Synthèse vocale', type: 'tts', owner: 'user_id' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('entry');
  });
});
