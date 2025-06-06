// Test unitaire pour sample_utils.js
const { add } = require('./sample_utils');
test('add fonctionne', () => {
  expect(add(2, 3)).toBe(5);
});
