// securityHelpers.js
// Helpers avancés pour la sécurité webApp (XSS, JWT, permissions)

/**
 * Échappe une chaîne pour éviter les failles XSS
 * @param {string} str
 * @returns {string}
 */
export function escapeHTML(str) {
  return str.replace(/[&<>'"]/g, tag => ({'&':'&amp;','<':'&lt;','>':'&gt;','\'':'&#39;','"':'&quot;'}[tag]));
}

/**
 * Vérifie un token JWT (structure uniquement, pas la signature)
 * @param {string} token
 * @returns {boolean}
 */
export function isValidJWT(token) {
  return /^([\w-]+\.){2}[\w-]+$/.test(token);
}
