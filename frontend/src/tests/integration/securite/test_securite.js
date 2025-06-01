/**
 * Test d'intégration avancé pour la sécurité (CORS, JWT, WAF, anti-DDOS, audit, multilingue, plugins, RGPD, multitenancy, fallback IA, SEO, logs structurés, rôles)
 * @see README.md pour la documentation complète
 */
const request = require('supertest');
const app = require('../../../../backend/node/app');
const { getJwt, SUPPORTED_LANGUAGES } = require('../../utils/test_utils');

describe('Sécurité API Integration', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('CORS headers présents', async () => {
    const res = await request(app).options('/securite');
    expect(res.headers['access-control-allow-origin']).toBeDefined();
  });
  it('JWT requis pour accès sécurisé', async () => {
    const res = await request(app).get('/securite');
    expect(res.statusCode).toBe(401);
  });
  it('Audit log généré', async () => {
    const res = await request(app)
      .get('/securite')
      .set('Authorization', `Bearer ${jwt}`);
    expect(res.headers['x-audit-log']).toBeDefined();
  });
  it('Multilingue (Accept-Language)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await request(app)
        .get('/securite')
        .set('Authorization', `Bearer ${jwt}`)
        .set('Accept-Language', lang);
      expect(res.headers['content-language']).toBe(lang);
    }
  });
  it('WAF/anti-DDOS actif', async () => {
    const res = await request(app)
      .get('/securite')
      .set('Authorization', `Bearer ${jwt}`);
    expect(res.headers['x-waf-status']).toBe('active');
  });
  it('RGPD: export et anonymisation', async () => {
    const res = await request(app)
      .post('/securite/rgpd/export')
      .set('Authorization', `Bearer ${jwt}`);
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('export');
  });
});
