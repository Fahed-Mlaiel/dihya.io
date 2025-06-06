// __init__.test.js – Test d'import du point d'entrée models (fixtures/core/samples)
const { sampleModelsUltra } = require('./sample_models');
test('import sampleModelsUltra', () => {
  expect(typeof sampleModelsUltra).toBe('function');
});
