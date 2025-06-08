// test_usage_samples.js – Test ultra avancé pour usage_samples.js (guides.helpers.samples)
const { getUsageSample } = require('./usage_samples');

test('getUsageSample() retourne un objet avec status ok et data', () => {
  const sample = getUsageSample();
  expect(sample.status).toBe('ok');
  expect(sample).toHaveProperty('data');
});
