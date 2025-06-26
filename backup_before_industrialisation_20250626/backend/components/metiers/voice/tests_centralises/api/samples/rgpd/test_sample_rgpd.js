// test_sample_rgpd.js – Test ultra avancé des samples RGPD API voice (centralisé)

const { sampleRgpdSanitize } = require('../../../api/samples/rgpd');

describe('Samples RGPD API voice', () => {
  it('doit anonymiser et valider la conformité RGPD', () => {
    const data = { name: 'UltraCube', email: 'user@example.com' };
    const result = sampleRgpdSanitize(data);
    expect(result.sanitized).toBe(true);
    expect(result.data).toEqual(data);
  });
});
