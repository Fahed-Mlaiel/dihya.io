// partials_views.js – Helpers et fragments réutilisables (partials) pour le module vr_ar
// Widgets, composants, conformité RGPD, accessibilité, audit, i18n
function renderWidget(name, data) {
  return `<div class='widget widget-${name}'>${data}</div>`;
}

module.exports = { renderWidget };
