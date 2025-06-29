// test_sample_validators.js – Test ultra avancé des samples validators API Banque_Finance (centralisé)

const { sampleValidatorUltra } = require('../../../api/samples/validators');

describe('Samples Validators API Banque_Finance', () => {
  it('doit valider les données métier ultra avancées', () => {
    const data = { name: 'UltraCube', status: 'active' };
    const result = sampleValidatorUltra(data);
    expect(result.valid).toBe(true);
    expect(result.data).toEqual(data);
  });
});
