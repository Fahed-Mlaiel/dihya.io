// test_rgpd.js – Test ultra avancé RGPD API administration_publique (centralisé)

const { sampleRgpdSanitize } = require('../../../api/samples/rgpd');

describe('RGPD API administration_publique', () => {
  it('doit anonymiser et valider la conformité RGPD', () => {
    const data = { name: 'UltraCube', email: 'user@example.com' };
    const result = sampleRgpdSanitize(data);
    expect(result.sanitized).toBe(true);
    expect(result.data).toEqual(data);
  });
});
