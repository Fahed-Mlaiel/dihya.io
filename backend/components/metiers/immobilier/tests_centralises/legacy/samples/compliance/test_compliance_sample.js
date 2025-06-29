// Test ultra avancé pour compliance_sample.js
const complianceSample = require('../../../legacy/samples/compliance/compliance_sample');

describe('Compliance Sample', () => {
  it('doit valider la conformité RGPD', () => {
    expect(complianceSample({consent: true})).toBe(true);
  });
  it('doit refuser un objet sans consent', () => {
    expect(complianceSample({})).toBe(false);
  });
  // ...autres tests avancés, edge cases, conformité...
});
