// test_rgpd.js – Test ultra avancé RGPD API Immobilier (centralisé)

const { sampleRgpdSanitize } = require('../../../api/samples/rgpd');

describe('RGPD API Immobilier', () => {
  it('doit anonymiser et valider la conformité RGPD', () => {
    const data = { name: 'UltraBien', email: 'user@example.com' };
    const result = sampleRgpdSanitize(data);
    expect(result.sanitized).toBe(true);
    expect(result.data).toEqual(data);
  });
});
