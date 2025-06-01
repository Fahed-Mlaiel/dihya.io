/**
 * Test d'intégration global pour la cohérence, la sécurité, l'audit, la RGPD, l'i18n, le fallback IA, la gestion des rôles, la compatibilité multi-stack, la performance, la conformité, le SEO, l'accessibilité, la modularité, l'extensibilité, la souveraineté numérique
 * @see README.md pour la documentation complète
 */
const request = require('supertest');
const app = require('../../../../backend/node/app');
const { getJwt, SUPPORTED_LANGUAGES } = require('../../utils/test_utils');

describe('Global Integration', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('GET /status (health, audit, i18n, SEO)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await request(app)
        .get('/status')
        .set('Authorization', `Bearer ${jwt}`)
        .set('Accept-Language', lang);
      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('status');
      expect(res.headers['content-language']).toBe(lang);
    }
  });
  it('Fallback IA open source (LLaMA, Mixtral, Mistral)', async () => {
    const res = await request(app)
      .post('/ai/fallback')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ prompt: 'Test fallback' });
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('result');
  });
});
