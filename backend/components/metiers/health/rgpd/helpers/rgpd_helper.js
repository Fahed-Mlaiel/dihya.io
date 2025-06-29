// rgpd_helper.js – Helper RGPD (JS)
/**
 * Exemple de helper RGPD
 */
function maskPII(data) {
  if (typeof data !== 'object' || data === null) {
    throw new Error('Data must be a non-null object');
  }
  return { ...data, masked: true };
}

module.exports = { maskPII };
