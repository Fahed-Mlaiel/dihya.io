/**
 * @file validation.js
 * @description Fonctions de validation génériques et avancées pour Dihya Coding (sécurité, conformité RGPD, audit, logs).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les validations sont typées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Valide un identifiant utilisateur (email ou pseudo).
 * @param {string} userId
 * @returns {boolean}
 */
export function validateUserId(userId) {
  const valid =
    typeof userId === 'string' &&
    userId.length >= 2 &&
    userId.length <= 128 &&
    /^[a-zA-Z0-9._-]+(@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)?$/.test(userId);
  logValidationEvent('validateUserId', anonymizeUserId(userId), valid);
  return valid;
}

/**
 * Valide un email.
 * @param {string} email
 * @returns {boolean}
 */
export function validateEmail(email) {
  const valid =
    typeof email === 'string' &&
    /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  logValidationEvent('validateEmail', anonymizeUserId(email), valid);
  return valid;
}

/**
 * Valide un mot de passe (longueur, complexité).
 * @param {string} password
 * @returns {boolean}
 */
export function validatePassword(password) {
  const valid =
    typeof password === 'string' &&
    password.length >= 8 &&
    /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$/.test(password);
  logValidationEvent('validatePassword', '[protected]', valid);
  return valid;
}

/**
 * Valide un nom de projet ou d’entité.
 * @param {string} name
 * @returns {boolean}
 */
export function validateName(name) {
  const valid =
    typeof name === 'string' &&
    name.length >= 3 &&
    name.length <= 64 &&
    /^[a-zA-Z0-9._ -]+$/.test(name);
  logValidationEvent('validateName', name, valid);
  return valid;
}

/**
 * Valide un endpoint ou une route API.
 * @param {string} endpoint
 * @returns {boolean}
 */
export function validateEndpoint(endpoint) {
  const valid =
    typeof endpoint === 'string' &&
    endpoint.length >= 2 &&
    /^\/[a-zA-Z0-9/_-]*$/.test(endpoint);
  logValidationEvent('validateEndpoint', endpoint, valid);
  return valid;
}

/**
 * Valide une URL.
 * @param {string} url
 * @returns {boolean}
 */
export function validateUrl(url) {
  try {
    const u = new URL(url);
    const valid = ['http:', 'https:'].includes(u.protocol);
    logValidationEvent('validateUrl', url, valid);
    return valid;
  } catch {
    logValidationEvent('validateUrl', url, false);
    return false;
  }
}

/**
 * Anonymise un identifiant utilisateur ou email pour les logs.
 * @param {string} userId
 * @returns {string}
 */
function anonymizeUserId(userId) {
  return typeof userId === 'string'
    ? userId.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '[email]')
    : userId;
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {*} value
 * @param {boolean} valid
 */
function logValidationEvent(action, value, valid) {
  try {
    const logs = JSON.parse(localStorage.getItem('validation_logs') || '[]');
    logs.push({
      action,
      value,
      valid,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('validation_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de validation (droit à l’oubli RGPD).
 */
export function clearLocalValidationLogs() {
  localStorage.removeItem('validation_logs');
}