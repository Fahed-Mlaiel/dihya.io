const sample = require('./sample_advanced');
describe('Sample Advanced Example', () => {
  it('should have auditor role', () => {
    expect(sample.role).toBe('auditor');
  });
});
