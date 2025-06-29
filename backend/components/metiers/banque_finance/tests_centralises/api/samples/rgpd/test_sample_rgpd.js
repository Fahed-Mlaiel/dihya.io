// test_sample_rgpd.js – Test ultra avancé des samples RGPD API Banque_Finance (centralisé)

const { sampleRgpdSanitize } = require('../../../api/samples/rgpd');

describe('Samples RGPD API Banque_Finance', () => {
  it('doit anonymiser et valider la conformité RGPD', () => {
    const data = { name: 'UltraCube', email: 'user@example.com' };
    const result = sampleRgpdSanitize(data);
    expect(result.sanitized).toBe(true);
    expect(result.data).toEqual(data);
  });
});
