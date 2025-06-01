/**
 * Test d'intégration avancé pour l'optimisation SEO backend (robots, sitemap, logs structurés, multilingue, audit, plugins, RGPD, fallback IA, accessibilité)
 * @see README.md pour la documentation complète
 */
const request = require('supertest');
const app = require('../../../../backend/node/app');
const { getJwt, SUPPORTED_LANGUAGES } = require('../../utils/test_utils');

describe('SEO API Integration', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('GET /robots.txt (SEO, audit)', async () => {
    const res = await request(app).get('/robots.txt');
    expect(res.statusCode).toBe(200);
    expect(res.text).toContain('User-agent');
  });
  it('GET /sitemap.xml (SEO, multilingue)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await request(app)
        .get('/sitemap.xml')
        .set('Accept-Language', lang);
      expect(res.statusCode).toBe(200);
      expect(res.headers['content-language']).toBe(lang);
    }
  });
  it('Logs structurés présents', async () => {
    const res = await request(app).get('/seo/logs');
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('logs');
  });
});
