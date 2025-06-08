// rgpd_helper.js – Helper RGPD (JS)
/**
 * Exemple de helper RGPD
 */
function maskPII(data) {
  // TODO: Implémenter la logique de masquage RGPD
  return { ...data, masked: true };
}

module.exports = { maskPII };
