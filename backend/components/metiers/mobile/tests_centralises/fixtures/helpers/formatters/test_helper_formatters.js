// test_helper_formatters.js – Tests helpers formatters (JS)
const { formatDate } = require('../../../../fixtures/helpers/formatters/helper_formatters');
test('formatDate', () => {
  expect(formatDate('2025-06-09T12:00:00')).toBe('2025-06-09T12:00:00.000Z');
});
