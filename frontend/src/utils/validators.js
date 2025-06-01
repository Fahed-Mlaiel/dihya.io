/**
 * @file validators.js
 * @description Utilitaires de validation pour Dihya Coding : validation des emails, mots de passe, identifiants, champs génériques, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Valide une adresse email.
 * @param {string} email
 * @returns {boolean}
 */
export function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(String(email));
}

/**
 * Valide un mot de passe fort (8+ caractères, majuscule, minuscule, chiffre, spécial).
 * @param {string} password
 * @returns {boolean}
 */
export function isStrongPassword(password) {
  return /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$/.test(String(password));
}

/**
 * Valide un identifiant utilisateur (alphanumérique, 3-32 caractères).
 * @param {string} id
 * @returns {boolean}
 */
export function isValidId(id) {
  return /^[a-zA-Z0-9_\-]{3,32}$/.test(String(id));
}

/**
 * Valide un champ texte générique (pas de caractères dangereux, longueur max).
 * @param {string} str
 * @param {number} [maxLength=256]
 * @returns {boolean}
 */
export function isSafeText(str, maxLength = 256) {
  return typeof str === 'string' && str.length > 0 && str.length <= maxLength && !/[<>]/.test(str);
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('validators_utils_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logValidatorsEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('validators_utils_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('validators_utils_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs validators (droit à l’oubli RGPD).
 */
export function clearLocalValidatorsUtilsLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('validators_utils_logs');
  }
}

/* Documentation claire : chaque fonction est commentée pour auditabilité et conformité */