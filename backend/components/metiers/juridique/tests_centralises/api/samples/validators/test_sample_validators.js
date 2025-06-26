// test_sample_validators.js – Test ultra avancé des samples validators API Juridique (centralisé)

const { sampleValidatorUltra } = require('../../../api/samples/validators');

describe('Samples Validators API Juridique', () => {
  it('doit valider les données métier ultra avancées', () => {
    const data = { name: 'UltraDossier', status: 'active' };
    const result = sampleValidatorUltra(data);
    expect(result.valid).toBe(true);
    expect(result.data).toEqual(data);
  });
});
