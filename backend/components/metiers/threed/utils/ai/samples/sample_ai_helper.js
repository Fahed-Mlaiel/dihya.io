// sample_ai_helper.js – Exemple de helper IA (JS)
function sampleAiHelper(input) {
  if (!input) return { status: 'ERROR', reason: 'no input' };
  return { status: 'SAMPLE', data: input, audit: true };
}
module.exports = { sampleAiHelper };
