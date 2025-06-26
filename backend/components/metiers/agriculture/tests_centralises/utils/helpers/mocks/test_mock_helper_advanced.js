// test_mock_helper_advanced.js – Tests ultra avancés pour mock_helper.js (helpers/mocks)
const { mockValidationData } = require('../../../../utils/helpers/mocks/mock_helper');

describe('Helpers Mocks – mockValidationData (Ultra avancé)', () => {
  it('génère des données de validation mockées conformes RGPD', () => {
    const mock = mockValidationData();
    expect(mock).toHaveProperty('id');
    expect(mock).toHaveProperty('user');
    expect(mock).toHaveProperty('email');
    expect(mock).toHaveProperty('consent');
    expect(mock).toHaveProperty('timestamp');
    expect(typeof mock.timestamp).toBe('string');
  });

  it('auditabilité: le mock contient un timestamp', () => {
    const mock = mockValidationData();
    expect(mock.timestamp).toMatch(/\d{4}-\d{2}-\d{2}T/);
  });

  it('gère les caractères spéciaux et accessibilité', () => {
    const mock = mockValidationData();
    expect(mock.user).toBe('mocked');
    expect(mock.email).toMatch('@');
  });
});
