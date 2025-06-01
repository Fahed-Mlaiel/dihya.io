/**
 * @file headersConfig.js
 * @description Configuration des headers HTTP de sécurité pour Dihya Coding : sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Génère une configuration de headers HTTP sécurisés.
 * @param {object} [params]
 * @param {object} [params.customHeaders] - Headers additionnels à ajouter
 * @param {object} [params.options] - Options avancées (logs, RGPD, etc.)
 * @returns {object} Objet de configuration des headers
 */
export function getHeadersConfig({
  customHeaders = {},
  options = {}
} = {}) {
  const defaultHeaders = {
    'X-Content-Type-Options': 'nosniff',
    'X-Frame-Options': 'SAMEORIGIN',
    'X-XSS-Protection': '1; mode=block',
    'Referrer-Policy': 'strict-origin-when-cross-origin',
    'Permissions-Policy': 'geolocation=(), microphone=(), camera=()',
    'Strict-Transport-Security': 'max-age=63072000; includeSubDomains; preload',
    'Content-Security-Policy': "default-src 'self'; script-src 'self'; object-src 'none'; frame-ancestors 'self'; base-uri 'self';"
  };

  const headers = { ...defaultHeaders, ...sanitizeHeaders(customHeaders) };

  if (options.log !== false && hasConsent()) {
    logHeadersConfigEvent('headers_config_generated', {
      headers: anonymizeHeaders(headers),
      timestamp: new Date().toISOString()
    });
  }

  return headers;
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('headers_config_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logHeadersConfigEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('headers_config_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('headers_config_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Sanitize les headers pour éviter l’injection.
 * @param {object} headers
 * @returns {object}
 */
function sanitizeHeaders(headers) {
  const sanitized = {};
  Object.entries(headers || {}).forEach(([k, v]) => {
    sanitized[String(k).replace(/[^a-zA-Z0-9\-]/g, '')] = String(v).replace(/[\r\n]/g, '');
  });
  return sanitized;
}

/**
 * Anonymise les headers pour les logs.
 * @param {object} headers
 * @returns {object}
 */
function anonymizeHeaders(headers) {
  const anonymized = {};
  Object.keys(headers || {}).forEach((k) => {
    anonymized[k] = headers[k].length > 32 ? headers[k].slice(0, 16) + '...' : headers[k];
  });
  return anonymized;
}

/**
 * Efface les logs headers (droit à l’oubli RGPD).
 */
export function clearLocalHeadersConfigLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('headers_config_logs');
  }
}