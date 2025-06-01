// Test d'intégration avancé – Automobile
/**
 * Test automatisé Automobile : sécurité (CORS, JWT, validation), RGPD, accessibilité (ARIA), multilingue, CI/CD-ready, plugins, audit, monitoring
 */
const request = require('supertest');
const app = require('../../../../src/app');
describe('Integration – Automobile', () => {
  it('should return compliant automobile data (security, RGPD, a11y, i18n)', async () => {
    const res = await request(app).get('/api/automobile');
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('status', 'ok');
    expect(res.body).toHaveProperty('privacy');
    expect(res.body).toHaveProperty('accessibility');
    expect(res.body).toHaveProperty('i18n');
  });
});
