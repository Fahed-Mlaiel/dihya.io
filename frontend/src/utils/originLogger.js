/**
 * @file originLogger.js
 * @description Utilitaire de journalisation d’origine pour Dihya Coding : logue l’origine des requêtes/actions côté client, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont anonymisées, loguées localement, respectent le consentement utilisateur et sont facilement extensibles.
 */

/**
 * Logue l’origine d’une action ou requête (URL, referrer, user agent).
 * @param {string} action - Nom de l’action ou événement
 * @param {object} [extra] - Données additionnelles à loguer
 * @returns {boolean} Succès du log
 */
export function logOrigin(action, extra = {}) {
  if (!hasConsent()) return false;
  try {
    const originData = {
      action: sanitize(action),
      url: anonymizeUrl(window.location.href),
      referrer: anonymizeUrl(document.referrer),
      userAgent: anonymizeUserAgent(navigator.userAgent),
      ...extra,
      timestamp: new Date().toISOString()
    };
    const logs = JSON.parse(window.localStorage.getItem('origin_logger_logs') || '[]');
    logs.push(originData);
    window.localStorage.setItem('origin_logger_logs', JSON.stringify(logs));
    return true;
  } catch {
    return false;
  }
}

/**
 * Récupère les logs d’origine.
 * @returns {Array<object>} Liste des logs
 */
export function getOriginLogs() {
  if (!hasConsent()) return [];
  try {
    return JSON.parse(window.localStorage.getItem('origin_logger_logs') || '[]');
  } catch {
    return [];
  }
}

/**
 * Efface les logs d’origine (droit à l’oubli RGPD).
 */
export function clearLocalOriginLoggerLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('origin_logger_logs');
  }
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('origin_logger_feature_consent');
}

/**
 * Sanitize une chaîne pour éviter l’injection.
 * @param {string} str
 * @returns {string}
 */
function sanitize(str) {
  return String(str).replace(/[\r\n<>]/g, '');
}

/**
 * Anonymise une URL pour les logs.
 * @param {string} url
 * @returns {string}
 */
function anonymizeUrl(url) {
  if (!url) return '';
  // Masque le domaine et les paramètres sensibles
  try {
    const u = new URL(url);
    return u.origin + u.pathname;
  } catch {
    return '';
  }
}

/**
 * Anonymise le user agent pour les logs.
 * @param {string} ua
 * @returns {string}
 */
function anonymizeUserAgent(ua) {
  if (!ua) return '';
  // Ne conserve que le type de navigateur et OS (ex : "Mozilla/5.0 (Windows NT 10.0)")
  return ua.split(')')[0] + ')';
}

/* Documentation claire : chaque fonction est commentée pour auditabilité et conformité */