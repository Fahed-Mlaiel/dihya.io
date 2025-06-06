// index.test.js – Test d’import du point d’entrée JS legacy/fallback
const fallback = require('./index');
test('import index.js legacy/fallback', () => {
  expect(fallback).toBeDefined();
});
