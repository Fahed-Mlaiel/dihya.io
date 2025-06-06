// Test du helper d’exemple (JS)
const { sampleHelper } = require('./sample_helper');
describe('sampleHelper', () => {
  it('should log and return true', () => {
    expect(sampleHelper('exemple')).toBe(true);
  });
});
