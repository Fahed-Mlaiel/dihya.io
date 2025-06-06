// __init__.test.js – Test d'import du point d'entrée JS docs (guides/core/samples/docs)
const docs = require('./__init__');
test('import docs entrypoint (__init__.js)', () => {
  expect(docs.sampleGuideDoc).toBeDefined();
});
