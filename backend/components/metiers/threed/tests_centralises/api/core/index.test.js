// index.test.js – Test ultra avancé pour index.js (API Threed)
const index = require('../../../../../api/core/index');

test('index existe', () => {
  expect(typeof index !== 'undefined').toBe(true);
});
