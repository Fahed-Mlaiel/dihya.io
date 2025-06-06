// index.test.js – Test d’intégration du point d’entrée global des tests Threed
const entry = require('./index.js');
describe('Entrée globale tests Threed', () => {
  it('expose tous les sous-modules de test', () => {
    expect(entry.api).toBeDefined();
    expect(entry.fixtures).toBeDefined();
    expect(entry.guides).toBeDefined();
    expect(entry.integration).toBeDefined();
    expect(entry.legacy).toBeDefined();
    expect(entry.plugins).toBeDefined();
    expect(entry.rgpd).toBeDefined();
    expect(entry.security).toBeDefined();
    expect(entry.services).toBeDefined();
    expect(entry.templates).toBeDefined();
    expect(entry.utils).toBeDefined();
  });
});
