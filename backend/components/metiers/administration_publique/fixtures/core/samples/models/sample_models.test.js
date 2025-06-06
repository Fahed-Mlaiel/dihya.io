// sample_models.test.js – Test ultra avancé pour sampleModels (JS)
const sampleModelsUltra = require('./sample_models');
test('sampleModelsUltra fonctionne sans erreur', () => {
  expect(() => sampleModelsUltra()).not.toThrow();
});
