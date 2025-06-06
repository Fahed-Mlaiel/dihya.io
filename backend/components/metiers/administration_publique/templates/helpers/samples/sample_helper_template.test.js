// sample_helper_template.test.js – Test JS exemple helper template
const { sampleHelperTemplate } = require('./sample_helper_template');
test('sampleHelperTemplate fonctionne', () => {
  expect(sampleHelperTemplate({ a: 1 })).toEqual({ a: 1, helper: true });
  expect(sampleHelperTemplate()).toEqual({ helper: true, empty: true });
});
