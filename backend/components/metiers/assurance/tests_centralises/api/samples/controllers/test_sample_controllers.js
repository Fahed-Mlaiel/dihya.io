// test_sample_controllers.js – Test ultra avancé des samples contrôleurs API Assurance (centralisé)

const { sampleControllerUltra } = require('../../../api/samples/controllers');

describe('Samples Contrôleurs API Assurance', () => {
  it('doit exécuter le contrôleur ultra avancé avec succès', () => {
    const result = sampleControllerUltra();
    expect(result).toHaveProperty('created');
    expect(result.status).toBe('success');
    expect(result.created).toHaveProperty('name');
    expect(result.created).toHaveProperty('status');
    expect(result.created).toHaveProperty('label');
    expect(result.created).toHaveProperty('lang');
  });
});
