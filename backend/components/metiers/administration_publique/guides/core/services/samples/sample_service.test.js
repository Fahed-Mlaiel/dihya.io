// Test unitaire pour sample_service.js
const { run } = require('./sample_service');
test('run fonctionne', () => {
  expect(run()).toBe('Service exécuté!');
});
