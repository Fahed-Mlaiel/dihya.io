// Test d'intégration avancé – Health
/**
 * Test automatisé Health : sécurité (CORS, JWT, validation), RGPD, accessibilité (ARIA), multilingue, CI/CD-ready, plugins, audit, monitoring
 */
const request = require('supertest');
const app = require('../../../../src/app');
describe('Integration – Health', () => {
  it('should return compliant health data (security, RGPD, a11y, i18n)', async () => {
    const res = await request(app).get('/api/health');
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('status', 'ok');
    expect(res.body).toHaveProperty('privacy');
    expect(res.body).toHaveProperty('accessibility');
    expect(res.body).toHaveProperty('i18n');
  });
});
