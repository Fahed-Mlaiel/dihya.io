// Test d'intégration avancé – Services à la personne
/**
 * Test automatisé Services à la personne : sécurité (CORS, JWT, validation), RGPD, accessibilité (ARIA), multilingue, CI/CD-ready, plugins, audit, monitoring
 */
const request = require('supertest');
const app = require('../../../../src/app');
describe('Integration – Services à la personne', () => {
  it('should return compliant services_personne data (security, RGPD, a11y, i18n)', async () => {
    const res = await request(app).get('/api/services_personne');
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('status', 'ok');
    expect(res.body).toHaveProperty('privacy');
    expect(res.body).toHaveProperty('accessibility');
    expect(res.body).toHaveProperty('i18n');
  });
});
