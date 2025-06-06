// Test unitaire pour sample_validator.js
const { sampleValidatorUsage } = require('./sample_validator');
test('sampleValidatorUsage fonctionne', () => {
  expect(sampleValidatorUsage()).toBe('sample validator usage');
});
