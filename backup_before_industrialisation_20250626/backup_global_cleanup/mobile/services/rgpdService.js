// Service RGPD : anonymisation, consentement, export
/**
 * Anonymise un utilisateur
 * @param {object} user
 * @returns {object} Utilisateur anonymisé
 */
export function anonymizeUser(user) {
  return { ...user, name: 'Anonyme', email: null };
}

/**
 * Gère le consentement utilisateur
 * @param {string} userId
 * @param {boolean} consent
 */
export function setConsent(userId, consent) {
  // À brancher sur un vrai système de consentement
  console.log(`[CONSENT] ${userId}: ${consent}`);
}
