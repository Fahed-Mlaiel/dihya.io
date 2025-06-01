// Tests d'intégration E2E avancés pour l'API Dihya (Node.js)
const request = require('supertest');
const { getJwtTokenForRole } = require('../../security/jwt');
const app = require('../../main').app;

describe('API Dihya - Intégration E2E', () => {
  let adminToken, userToken;
  beforeAll(async () => {
    adminToken = await getJwtTokenForRole('admin');
    userToken = await getJwtTokenForRole('user');
  });

  test('GET /api/seo/robots.txt - SEO robots', async () => {
    const res = await request(app).get('/api/seo/robots.txt');
    expect(res.statusCode).toBe(200);
    expect(res.text).toContain('User-agent');
  });

  test('GET /api/audit/logs - Audit log', async () => {
    const res = await request(app)
      .get('/api/audit/logs')
      .set('Authorization', `Bearer ${adminToken}`);
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });

  test('POST /api/ia/fallback - Fallback IA', async () => {
    const res = await request(app)
      .post('/api/ia/fallback')
      .send({ question: 'Test fallback', lang: 'fr' })
      .set('Authorization', `Bearer ${adminToken}`);
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('answer');
  });

  test('GET /api/plugins/active - Plugins actifs', async () => {
    const res = await request(app)
      .get('/api/plugins/active')
      .set('Authorization', `Bearer ${adminToken}`);
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('seo');
  });

  test('GET /api/utils/healthcheck - Healthcheck', async () => {
    const res = await request(app).get('/api/utils/healthcheck');
    expect(res.statusCode).toBe(200);
    expect(res.body.status).toBe('ok');
  });

  test('GET /api/seo/sitemap.xml - Sitemap dynamique', async () => {
    const res = await request(app).get('/api/seo/sitemap.xml');
    expect(res.statusCode).toBe(200);
    expect(res.text).toContain('<urlset');
  });

  test('GET /api/validators/email - Validation email', async () => {
    const res = await request(app)
      .post('/api/validators/email')
      .send({ email: 'test@dihya.ai' });
    expect(res.statusCode).toBe(200);
    expect(res.body.valid).toBe(true);
  });
});
