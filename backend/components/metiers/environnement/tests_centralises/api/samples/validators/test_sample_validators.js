// test_sample_validators.js – Test ultra avancé des samples validators API Environnement (centralisé)

const { sampleValidatorUltra } = require('../../../api/samples/validators');

describe('Samples Validators API Environnement', () => {
  it('doit valider les données métier ultra avancées', () => {
    const data = { name: 'UltraCube', status: 'active' };
    const result = sampleValidatorUltra(data);
    expect(result.valid).toBe(true);
    expect(result.data).toEqual(data);
  });
});
