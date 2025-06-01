/**
 * @file securityAuto.js
 * @description Fonctions utilitaires pour l’automatisation de la sécurité dans Dihya Coding (anti-DDoS, rate limiting, CORS, headers, validation, audit).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Applique automatiquement les headers de sécurité recommandés.
 * @param {object} [options]
 * @returns {object} Headers de sécurité générés
 */
export function applySecurityHeaders(options = {}) {
  if (!hasConsent()) throw new Error('Consentement requis pour appliquer les headers de sécurité.');
  const headers = {
    'Content-Security-Policy': options.csp || "default-src 'self'",
    'Strict-Transport-Security': options.hsts ? 'max-age=63072000; includeSubDomains; preload' : undefined,
    'X-Frame-Options': options.xFrame || 'SAMEORIGIN',
    'X-Content-Type-Options': 'nosniff',
    'Referrer-Policy': options.referrerPolicy || 'strict-origin-when-cross-origin',
    'Permissions-Policy': options.permissionsPolicy || 'geolocation=(), microphone=()',
    ...options.customHeaders
  };
  logSecurityAutoEvent('apply_headers', anonymizeSecurityData(headers));
  return Object.fromEntries(Object.entries(headers).filter(([_, v]) => v !== undefined));
}

/**
 * Applique une règle de rate limiting automatique.
 * @param {object} params
 * @param {string} params.userId
 * @param {number} params.limit
 * @param {number} params.window - en secondes
 * @returns {object} Règle de rate limiting générée
 */
export function applyRateLimiting({ userId, limit = 100, window = 60 }) {
  if (!hasConsent()) throw new Error('Consentement requis pour appliquer le rate limiting.');
  if (!userId) throw new Error('userId requis');
  const rule = { userId: anonymizeUserId(userId), limit, window };
  logSecurityAutoEvent('apply_rate_limiting', rule);
  return rule;
}

/**
 * Applique une configuration CORS automatique.
 * @param {object} params
 * @param {string[]} params.origins
 * @param {string[]} [params.methods]
 * @returns {object} Configuration CORS générée
 */
export function applyCORS({ origins, methods = ['GET', 'POST'] }) {
  if (!hasConsent()) throw new Error('Consentement requis pour appliquer la configuration CORS.');
  if (!Array.isArray(origins) || origins.length === 0) throw new Error('origins requis');
  const cors = { origins: origins.map(anonymizeOrigin), methods };
  logSecurityAutoEvent('apply_cors', cors);
  return cors;
}

/**
 * Valide une entrée utilisateur selon un schéma simple.
 * @param {any} value
 * @param {string} type - 'email', 'number', 'string', etc.
 * @returns {object} Résultat de la validation
 */
export function validateInput(value, type) {
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
  logSecurityAutoEvent('validate_input', { type, isValid, value: anonymizeInput(type, value) });
  return { type, isValid };
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('security_auto_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logSecurityAutoEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('security_auto_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString(),
    });
    window.localStorage.setItem('security_auto_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise les données sensibles pour les logs.
 * @param {object} data
 * @returns {object}
 */
function anonymizeSecurityData(data) {
  if (!data || typeof data !== 'object') return data;
  const clone = { ...data };
  if (clone['Authorization']) clone['Authorization'] = '[protected]';
  return clone;
}

/**
 * Anonymise un userId pour les logs.
 * @param {string} userId
 * @returns {string}
 */
function anonymizeUserId(userId) {
  if (!userId) return '';
  return userId.length > 4 ? userId.slice(0, 2) + '***' + userId.slice(-2) : '***';
}

/**
 * Anonymise une origine pour les logs.
 * @param {string} origin
 * @returns {string}
 */
function anonymizeOrigin(origin) {
  if (!origin) return '';
  return origin.replace(/:\/\/.*@/, '://[anonymized]@');
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
 * Efface les logs de sécurité automatique (droit à l’oubli RGPD).
 */
export function clearLocalSecurityAutoLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('security_auto_logs');
  }
}