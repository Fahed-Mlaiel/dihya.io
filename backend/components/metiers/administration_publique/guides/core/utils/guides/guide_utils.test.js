// Tests unitaires pour guide_utils.js (JS)
const utils = require('./guide_utils');
test('doc existe', () => {
  expect(utils.doc).toBeDefined();
});
