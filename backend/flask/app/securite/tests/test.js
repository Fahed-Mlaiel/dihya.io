// Tests avancés pour la sécurité (Node.js)
const request = require('supertest');
const app = require('../../../../app');
const { mockJwt, mockRole, mockAudit } = require('../../utils/testUtils');

describe('Security API', () => {
  beforeAll(() => {
    mockJwt();
    mockRole('admin');
    mockAudit();
  });

  it('should allow admin access to secure endpoint', async () => {
    const res = await request(app)
      .get('/api/secure/admin')
      .set('Authorization', 'Bearer testtoken');
    expect(res.statusCode).toBe(200);
  });

  it('should block guest from admin endpoint', async () => {
    mockRole('guest');
    const res = await request(app)
      .get('/api/secure/admin')
      .set('Authorization', 'Bearer testtoken');
    expect(res.statusCode).toBe(403);
  });

  it('should enforce CORS policy', async () => {
    const res = await request(app)
      .options('/api/secure/admin')
      .set('Origin', 'https://evil.com');
    expect(res.headers['access-control-allow-origin']).not.toBe('https://evil.com');
  });

  // ...autres tests : WAF, anti-DDOS, RGPD, plugins, accessibilité, e2e, multilingue...
});
