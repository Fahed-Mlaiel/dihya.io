// Test ultra avancé pour rgpd_sample.js
const rgpdSample = require('../../../legacy/samples/rgpd/rgpd_sample');

describe('RGPD Sample', () => {
  it('doit exporter un utilisateur', () => {
    const result = rgpdSample('alice');
    expect(result.user).toBe('alice');
    expect(result.export).toBe(true);
    expect(typeof result.date).toBe('string');
  });
  it('doit exporter un utilisateur vide', () => {
    const result = rgpdSample('');
    expect(result.user).toBe('');
    expect(result.export).toBe(true);
    expect(typeof result.date).toBe('string');
  });
  it('doit exporter un utilisateur null', () => {
    const result = rgpdSample(null);
    expect(result.user).toBeNull();
    expect(result.export).toBe(true);
    expect(typeof result.date).toBe('string');
  });
  it('doit auditer le format de date ISO', () => {
    const result = rgpdSample('bob');
    expect(result.date).toMatch(/\d{4}-\d{2}-\d{2}T/);
  });
  // ...autres tests avancés, edge cases, conformité RGPD...
});
