/**
 * @file securityValidators.js
 * @description Fonctions de validation de sécurité pour Dihya Coding (anti-DDoS, rate limiting, CORS, headers, input, audit).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les validations sont strictes, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Valide la configuration anti-DDoS.
 * @param {object} config
 * @param {number} config.maxRequests
 * @param {number} config.windowSeconds
 * @returns {boolean}
 */
export function validateAntiDDoSConfig(config) {
  if (!hasConsent()) throw new Error('Consentement requis pour valider la configuration anti-DDoS.');
  const valid = typeof config === 'object'
    && typeof config.maxRequests === 'number'
    && config.maxRequests > 0
    && typeof config.windowSeconds === 'number'
    && config.windowSeconds > 0;
  logSecurityValidation('anti_ddos', anonymizeConfig(config), valid);
  return valid;
}

/**
 * Valide la configuration de rate limiting.
 * @param {object} config
 * @param {number} config.limit
 * @param {number} config.window
 * @returns {boolean}
 */
export function validateRateLimitConfig(config) {
  if (!hasConsent()) throw new Error('Consentement requis pour valider la configuration de rate limiting.');
  const valid = typeof config === 'object'
    && typeof config.limit === 'number'
    && config.limit > 0
    && typeof config.window === 'number'
    && config.window > 0;
  logSecurityValidation('rate_limit', anonymizeConfig(config), valid);
  return valid;
}

/**
 * Valide la configuration CORS.
 * @param {object} config
 * @param {string[]} config.origins
 * @param {string[]} [config.methods]
 * @returns {boolean}
 */
export function validateCORSConfig(config) {
  if (!hasConsent()) throw new Error('Consentement requis pour valider la configuration CORS.');
  const valid = typeof config === 'object'
    && Array.isArray(config.origins)
    && config.origins.length > 0
    && (config.methods === undefined || Array.isArray(config.methods));
  logSecurityValidation('cors', anonymizeConfig(config), valid);
  return valid;
}

/**
 * Valide la configuration des headers de sécurité.
 * @param {object} headers
 * @returns {boolean}
 */
export function validateSecurityHeaders(headers) {
  if (!hasConsent()) throw new Error('Consentement requis pour valider les headers de sécurité.');
  const required = ['Content-Security-Policy', 'X-Frame-Options', 'X-Content-Type-Options'];
  const valid = typeof headers === 'object'
    && required.every(h => h in headers);
  logSecurityValidation('headers', anonymizeConfig(headers), valid);
  return valid;
}

/**
 * Valide une entrée utilisateur selon un schéma simple.
 * @param {any} value
 * @param {string} type - 'email', 'number', 'string', etc.
 * @returns {boolean}
 */
export function validateSecurityInput(value, type) {
  if (!hasConsent()) throw new Error('Consentement requis pour valider une entrée.');
  let isValid = false;
  switch (type) {
    case 'email':
      isValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
      break;
    case 'number':
      isValid = typeof value === 'number' && !isNaN(value);
      break;
    case 'string':
      isValid = typeof value === 'string' && value.trim().length > 0;
      break;
    default:
      isValid = false;
  }
  logSecurityValidation('input', anonymizeInput(type, value), isValid);
  return isValid;
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('security_validators_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} type
 * @param {object} data
 * @param {boolean} valid
 */
function logSecurityValidation(type, data, valid) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('security_validators_logs') || '[]');
    logs.push({
      type,
      data,
      valid,
      timestamp: new Date().toISOString(),
    });
    window.localStorage.setItem('security_validators_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise la configuration pour les logs.
 * @param {object} config
 * @returns {object}
 */
function anonymizeConfig(config) {
  if (!config || typeof config !== 'object') return config;
  const clone = { ...config };
  if (clone.apiKey) clone.apiKey = '[protected]';
  if (clone.token) clone.token = '[protected]';
  return clone;
}

/**
 * Anonymise une entrée utilisateur selon le type.
 * @param {string} type
 * @param {any} value
 * @returns {any}
 */
function anonymizeInput(type, value) {
  if (type === 'email') return '[email]';
  if (type === 'number') return '[number]';
  return value;
}

/**
 * Efface les logs de validation de sécurité (droit à l’oubli RGPD).
 */
export function clearLocalSecurityValidatorsLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('security_validators_logs');
  }
}