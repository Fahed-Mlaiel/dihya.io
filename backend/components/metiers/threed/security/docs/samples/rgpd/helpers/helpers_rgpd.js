// helpers_rgpd.js
// Helpers avancés pour la conformité RGPD, privacy by design, consentement

function anonymizeData(data) {
  // Simule l'anonymisation de données personnelles
  return Object.fromEntries(Object.entries(data).map(([k, v]) => [k, '***']));
}

function checkConsent(user) {
  // Vérifie le consentement utilisateur
  return user && user.consent === true;
}

module.exports = { anonymizeData, checkConsent };
