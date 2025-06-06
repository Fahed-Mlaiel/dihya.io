// sample_helper_template.js – Exemple ultra avancé helper template
function sampleHelperTemplate(data) {
  if (!data) return { helper: true, empty: true };
  return { ...data, helper: true };
}
module.exports = { sampleHelperTemplate };
