// templates_views.js – Helpers et templates (HTML, Jinja, etc.) pour le module threed
// Rendu, conformité RGPD, accessibilité, audit, i18n
function renderTemplate(name, context) {
  return `<div class='template template-${name}'>${context}</div>`;
}

module.exports = { renderTemplate };
