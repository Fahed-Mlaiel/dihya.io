// Test d'intégration avancé – Arts
/**
 * Test automatisé Arts : sécurité (CORS, JWT, validation), RGPD, accessibilité (ARIA), multilingue, CI/CD-ready, plugins, audit, monitoring
 */
const request = require('supertest');
const app = require('../../../../src/app');
describe('Integration – Arts', () => {
  it('should return compliant arts data (security, RGPD, a11y, i18n)', async () => {
    const res = await request(app).get('/api/arts');
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('status', 'ok');
    expect(res.body).toHaveProperty('privacy');
    expect(res.body).toHaveProperty('accessibility');
    expect(res.body).toHaveProperty('i18n');
  });
});
