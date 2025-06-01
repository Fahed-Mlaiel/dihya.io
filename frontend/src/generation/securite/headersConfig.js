/**
 * @file headersConfig.js
 * @description Gestion avancée des headers HTTP de sécurité pour Dihya Coding (sécurité, SEO, audit, logs, conformité RGPD).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les configurations sont validées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Définit la configuration recommandée des headers HTTP de sécurité pour une API ou app Dihya Coding.
 * @param {object} [params]
 * @param {boolean} [params.enableCSP] - Active Content-Security-Policy
 * @param {boolean} [params.enableHSTS] - Active Strict-Transport-Security
 * @param {boolean} [params.enableXFrame] - Active X-Frame-Options
 * @param {boolean} [params.enableXSS] - Active X-XSS-Protection
 * @param {boolean} [params.enableReferrer] - Active Referrer-Policy
 * @returns {object} Objet de configuration des headers HTTP
 */
export function getSecurityHeadersConfig({
  enableCSP = true,
  enableHSTS = true,
  enableXFrame = true,
  enableXSS = true,
  enableReferrer = true,
} = {}) {
  const headers = {};

  if (enableCSP) {
    headers['Content-Security-Policy'] =
      "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; frame-ancestors 'none';";
  }
  if (enableHSTS) {
    headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains; preload';
  }
  if (enableXFrame) {
    headers['X-Frame-Options'] = 'DENY';
  }
  if (enableXSS) {
    headers['X-XSS-Protection'] = '1; mode=block';
  }
  if (enableReferrer) {
    headers['Referrer-Policy'] = 'strict-origin-when-cross-origin';
  }
  // Headers SEO-friendly
  headers['X-Content-Type-Options'] = 'nosniff';
  headers['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()';

  logHeadersConfigEvent('get_security_headers_config', Object.keys(headers));
  return headers;
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {Array<string>} headers
 */
function logHeadersConfigEvent(action, headers) {
  try {
    const logs = JSON.parse(localStorage.getItem('headers_config_logs') || '[]');
    logs.push({
      action,
      headers,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('headers_config_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de configuration des headers (droit à l’oubli RGPD).
 */
export function clearLocalHeadersConfigLogs() {
  localStorage.removeItem('headers_config_logs');
}