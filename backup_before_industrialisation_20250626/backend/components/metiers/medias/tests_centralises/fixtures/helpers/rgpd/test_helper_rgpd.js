// test_helper_rgpd.js – Tests helpers rgpd (JS)
const { anonymizeData } = require('../../../../fixtures/helpers/rgpd/helper_rgpd');
test('anonymizeData', () => {
  expect(anonymizeData({ a: 1, b: 2 })).toEqual({ a: '***', b: '***' });
});
