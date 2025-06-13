// rgpd_helper.js – Helper RGPD (JS)
/**
 * Exemple de helper RGPD
 */
function maskPII(data) {
  if (data === null || data === undefined) {
    throw new Error('Data cannot be null or undefined');
  }
  return { ...data, masked: true };
}

module.exports = { maskPII };
