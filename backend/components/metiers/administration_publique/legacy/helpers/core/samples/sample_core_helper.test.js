// Test unitaire pour sample_core_helper.js
const { sampleCoreUsage } = require('./sample_core_helper');
test('sampleCoreUsage fonctionne', () => {
  expect(sampleCoreUsage()).toBe('sample core usage');
});
