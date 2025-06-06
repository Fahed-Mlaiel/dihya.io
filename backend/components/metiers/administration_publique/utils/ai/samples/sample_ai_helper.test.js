// sample_ai_helper.test.js – Test unitaire ultra avancé sample helper IA (JS)
const { sampleAiHelper } = require('./sample_ai_helper');
test('sampleAiHelper retourne SAMPLE pour input', () => {
  const res = sampleAiHelper('foo');
  expect(res.status).toBe('SAMPLE');
  expect(res.data).toBe('foo');
  expect(res.audit).toBe(true);
});
test('sampleAiHelper retourne ERROR si pas d\'input', () => {
  const res = sampleAiHelper();
  expect(res.status).toBe('ERROR');
});
