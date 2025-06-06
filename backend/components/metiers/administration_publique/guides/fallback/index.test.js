// index.test.js – Test d'import du point d'entrée principal JS guides/fallback
const fallback = require('./index');
test('import fallback index.js', () => {
  expect(fallback).toBeDefined();
  expect(typeof fallback).toBe('object');
  expect(fallback.fallbackAccessibility || fallback.accessibility).toBeDefined();
  expect(fallback.fallbackPlugins || fallback.plugins).toBeDefined();
  expect(fallback.fallbackServices || fallback.services).toBeDefined();
  expect(fallback.samples).toBeDefined();
});
