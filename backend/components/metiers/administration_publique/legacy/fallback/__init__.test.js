const fallback = require('./__init__');
test('import __init__.js legacy/fallback', () => {
  expect(fallback).toBeDefined();
  expect(fallback.samples).toBeDefined();
});
