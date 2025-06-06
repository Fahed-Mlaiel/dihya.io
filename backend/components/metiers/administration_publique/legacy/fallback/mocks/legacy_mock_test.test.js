const { mockLegacyOperation } = require('./legacy_mock_test');

test('mockLegacyOperation renvoie mocked!', () => {
  expect(mockLegacyOperation()).toBe('mocked!');
});
