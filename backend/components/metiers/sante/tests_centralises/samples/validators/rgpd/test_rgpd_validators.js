// test_sample_rgpd.js
// Tests avancés pour sample_rgpd.js (validation RGPD)
const validateRGPD = require('../../../../samples/validators/rgpd/sample_rgpd');

describe('validateRGPD', () => {
  it('valide un objet avec hasConsent à true', () => {
    expect(validateRGPD({ hasConsent: true })).toBe(true);
  });
  it('rejette un objet avec hasConsent à false', () => {
    expect(validateRGPD({ hasConsent: false })).toBe(false);
  });
  it('rejette un objet sans hasConsent', () => {
    expect(validateRGPD({})).toBe(false);
  });
});
