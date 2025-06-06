// sample_helper_legacy.js – Exemple ultra avancé helper legacy
function sampleHelperLegacy(data) {
  if (!data) return { helper: true, empty: true };
  return { ...data, helper: true };
}
module.exports = { sampleHelperLegacy };
