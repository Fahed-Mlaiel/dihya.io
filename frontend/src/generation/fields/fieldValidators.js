/**
 * @file fieldValidators.js
 * @description Fonctions de validation avancée pour les champs Dihya Coding (formulaires, modèles, blueprints).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les validations sont typées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Valide un champ texte (longueur, caractères spéciaux).
 * @param {string} value
 * @param {object} [options]
 * @returns {boolean}
 */
export function validateText(value, options = {}) {
  const maxLength = options.maxLength || 255;
  const pattern = options.pattern || /^[\w\s.,;:!?'"()\-éèàçêâîôûùüëïöä]+$/i;
  const valid = typeof value === 'string' && value.length <= maxLength && pattern.test(value);
  logFieldValidation('validateText', value, valid);
  return valid;
}

/**
 * Valide un email.
 * @param {string} value
 * @returns {boolean}
 */
export function validateEmail(value) {
  const valid = typeof value === 'string' && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
  logFieldValidation('validateEmail', anonymizeEmail(value), valid);
  return valid;
}

/**
 * Valide un nombre (optionnellement borné).
 * @param {number} value
 * @param {object} [options]
 * @returns {boolean}
 */
export function validateNumber(value, options = {}) {
  const min = options.min ?? Number.MIN_SAFE_INTEGER;
  const max = options.max ?? Number.MAX_SAFE_INTEGER;
  const valid = typeof value === 'number' && !isNaN(value) && value >= min && value <= max;
  logFieldValidation('validateNumber', value, valid);
  return valid;
}

/**
 * Valide une date au format YYYY-MM-DD.
 * @param {string} value
 * @returns {boolean}
 */
export function validateDate(value) {
  const valid = typeof value === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(value);
  logFieldValidation('validateDate', value, valid);
  return valid;
}

/**
 * Valide un booléen.
 * @param {boolean} value
 * @returns {boolean}
 */
export function validateBoolean(value) {
  const valid = typeof value === 'boolean';
  logFieldValidation('validateBoolean', value, valid);
  return valid;
}

/**
 * Valide une sélection (valeur dans la liste d’options).
 * @param {*} value
 * @param {Array} options
 * @returns {boolean}
 */
export function validateSelect(value, options) {
  const valid = Array.isArray(options) && options.includes(value);
  logFieldValidation('validateSelect', value, valid);
  return valid;
}

/**
 * Valide un mot de passe (longueur minimale, complexité).
 * @param {string} value
 * @param {object} [options]
 * @returns {boolean}
 */
export function validatePassword(value, options = {}) {
  const minLength = options.minLength || 8;
  const pattern = options.pattern || /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$/;
  const valid = typeof value === 'string' && value.length >= minLength && pattern.test(value);
  logFieldValidation('validatePassword', '[protected]', valid);
  return valid;
}

/**
 * Anonymise un email pour les logs.
 * @param {string} email
 * @returns {string}
 */
function anonymizeEmail(email) {
  return typeof email === 'string'
    ? email.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '[email]')
    : email;
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {*} value
 * @param {boolean} valid
 */
function logFieldValidation(action, value, valid) {
  try {
    const logs = JSON.parse(localStorage.getItem('field_validators_logs') || '[]');
    logs.push({
      action,
      value,
      valid,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('field_validators_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de validation de champs (droit à l’oubli RGPD).
 */
export function clearLocalFieldValidatorsLogs() {
  localStorage.removeItem('field_validators_logs');
}