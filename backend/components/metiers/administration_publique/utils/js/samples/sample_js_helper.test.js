// Test du helper JS d’exemple (clé en main)
const { sampleJsHelper } = require('./sample_js_helper');
describe('sampleJsHelper', () => {
  it('should log and return true', () => {
    expect(sampleJsHelper('clé en main')).toBe(true);
  });
});
