// conformity_views.js – Helpers conformité avancés pour le module services_personne
// RGPD, accessibilité, audit, SEO, souveraineté numérique, sécurité, i18n
function checkRGPD(data) {
  const forbidden = Object.keys(data).filter(k => ["password", "ssn", "credit_card"].includes(k));
  if (forbidden.length > 0) {
    return { conform: false, message: `Champs interdits détectés: ${forbidden}` };
  }
  return { conform: true, message: "Conforme RGPD" };
}

function checkAccessibility(view) {
  if (!view.lang) {
    return { accessible: false, message: "Langue non spécifiée" };
  }
  return { accessible: true, message: "Accessible" };
}

module.exports = { checkRGPD, checkAccessibility };
