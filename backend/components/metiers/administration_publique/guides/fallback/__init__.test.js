// __init__.test.js – Test d'import du point d'entrée JS guides/fallback
const fallback = require('./__init__');
test('import fallback entrypoint (__init__.js)', () => {
  expect(fallback).toBeDefined();
  expect(typeof fallback).toBe('object');
});
