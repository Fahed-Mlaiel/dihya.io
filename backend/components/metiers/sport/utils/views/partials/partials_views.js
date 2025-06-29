// partials_views.js – Helpers et fragments réutilisables (partials) pour le module sport
// Widgets, composants, conformité RGPD, accessibilité, audit, i18n
function renderWidget(name, data) {
  return `<div class='widget widget-${name}'>${data}</div>`;
}

module.exports = { renderWidget };
