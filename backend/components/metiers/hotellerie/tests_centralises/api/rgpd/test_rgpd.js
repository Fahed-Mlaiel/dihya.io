// test_rgpd.js – Test ultra avancé RGPD API Hotellerie (centralisé)

const { sampleRgpdSanitize } = require('../../../api/samples/rgpd');

describe('RGPD API Hotellerie', () => {
  it('doit anonymiser et valider la conformité RGPD', () => {
    const data = { name: 'UltraCube', email: 'user@example.com' };
    const result = sampleRgpdSanitize(data);
    expect(result.sanitized).toBe(true);
    expect(result.data).toEqual(data);
  });
});
