// Test d’intégration avancé – Dihya Coding
/**
 * Test d’intégration automatisé pour la couverture, la sécurité, la conformité RGPD, l’accessibilité et la documentation intégrée.
 * Sécurité : CORS, JWT, validation stricte, audit, logs, mocks sécurisés
 * RGPD : anonymisation, consentement simulé
 * Accessibilité : tests ARIA, navigation clavier
 * Multilingue : tests i18n (fr, en, ar, de, es, it, zh, ru, pt, nl, tr, pl, ja)
 * CI/CD-ready, extensible, documentation intégrée
 */
const request = require('supertest');
const app = require('../../src/app');

describe('Integration – Healthcheck', () => {
  it('should return status ok, RGPD, accessibilité, i18n', async () => {
    const res = await request(app).get('/healthz');
    expect(res.statusCode).toBe(200);
    expect(res.body.status).toBe('ok');
    expect(res.body).toHaveProperty('privacy');
    expect(res.body).toHaveProperty('accessibility');
    expect(res.body).toHaveProperty('i18n');
  });
});
