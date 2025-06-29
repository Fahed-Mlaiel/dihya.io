// mock_helper.js – Mock ultra avancé helpers (clé en main)
/**
 * Mock de validation pour tests RGPD, audit, accessibilité
 * @returns {object}
 */
function mockValidationData() {
  return {
    id: 1,
    user: 'mocked',
    email: 'mock@example.com',
    consent: true,
    timestamp: new Date().toISOString()
  };
}
module.exports = { mockValidationData };
