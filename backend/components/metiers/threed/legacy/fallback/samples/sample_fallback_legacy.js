// sample_fallback_legacy.js – Exemple ultra avancé fallback legacy
function sampleFallbackLegacy(data) {
  if (!data) return { fallback: true, empty: true };
  return { ...data, fallback: true };
}
module.exports = { sampleFallbackLegacy };
