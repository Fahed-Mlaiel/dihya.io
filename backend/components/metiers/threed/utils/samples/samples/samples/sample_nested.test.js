// Test unitaire pour sample_nested.js
describe('Sample Nested', () => {
  it('should return a valid nested sample', () => {
    const { getNestedSample } = require('./sample_nested');
    const sample = getNestedSample();
    expect(sample.valid).toBe(true);
    expect(sample.level).toBe(3);
  });
});
