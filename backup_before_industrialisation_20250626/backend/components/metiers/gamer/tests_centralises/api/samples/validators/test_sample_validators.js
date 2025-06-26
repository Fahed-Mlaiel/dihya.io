// test_sample_validators.js – Test ultra avancé des samples validators API Gamer (centralisé)

const { sampleValidatorUltra } = require('../../../api/samples/validators');

describe('Samples Validators API Gamer', () => {
  it('doit valider les données métier ultra avancées', () => {
    const data = { name: 'UltraCube', status: 'active' };
    const result = sampleValidatorUltra(data);
    expect(result.valid).toBe(true);
    expect(result.data).toEqual(data);
  });
});
