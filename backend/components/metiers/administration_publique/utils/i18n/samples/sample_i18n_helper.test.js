// Test du helper i18n d’exemple (JS)
const { sampleI18n } = require('./sample_i18n_helper');
describe('sampleI18n', () => {
  it('should log and return true', () => {
    expect(sampleI18n('fr', 'Bonjour')).toBe(true);
  });
});
