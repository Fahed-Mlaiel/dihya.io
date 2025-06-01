/**
 * @file validation.js
 * @description Fonctions de validation pour Dihya Coding : validation sécurisée des entrées, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Valide une adresse email.
 * @param {string} email
 * @returns {boolean}
 */
export function validateEmail(email) {
  const valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  if (hasConsent()) {
    logValidationEvent('validate_email', { email: anonymizeEmail(email), valid, timestamp: new Date().toISOString() });
  }
  return valid;
}

/**
 * Valide un mot de passe (longueur, complexité).
 * @param {string} password
 * @param {object} [options]
 * @param {number} [options.minLength=8]
 * @param {boolean} [options.requireNumber=true]
 * @param {boolean} [options.requireSpecial=true]
 * @returns {boolean}
 */
export function validatePassword(password, options = {}) {
  const minLength = options.minLength || 8;
  const requireNumber = options.requireNumber !== false;
  const requireSpecial = options.requireSpecial !== false;
  let valid = typeof password === 'string' && password.length >= minLength;
  if (requireNumber) valid = valid && /\d/.test(password);
  if (requireSpecial) valid = valid && /[!@#$%^&*()_+\-=[\]{};':"\\|,.<>/?]/.test(password);
  if (hasConsent()) {
    logValidationEvent('validate_password', { valid, timestamp: new Date().toISOString() });
  }
  return valid;
}

/**
 * Valide un nom d’utilisateur (alphanumérique, 3-32 caractères).
 * @param {string} username
 * @returns {boolean}
 */
export function validateUsername(username) {
  const valid = typeof username === 'string' && /^[a-zA-Z0-9_]{3,32}$/.test(username);
  if (hasConsent()) {
    logValidationEvent('validate_username', { username: anonymizeUsername(username), valid, timestamp: new Date().toISOString() });
  }
  return valid;
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('validation_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logValidationEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('validation_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('validation_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise une adresse email pour les logs.
 * @param {string} email
 * @returns {string}
 */
function anonymizeEmail(email) {
  if (typeof email !== 'string') return '';
  const [user, domain] = email.split('@');
  return user ? user[0] + '***@' + (domain || '') : '[email]';
}

/**
 * Anonymise un nom d’utilisateur pour les logs.
 * @param {string} username
 * @returns {string}
 */
function anonymizeUsername(username) {
  if (!username) return '';
  return username.length > 4 ? username.slice(0, 2) + '***' + username.slice(-2) : '***';
}

/**
 * Efface les logs de validation (droit à l’oubli RGPD).
 */
export function clearLocalValidationLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('validation_logs');
  }
}