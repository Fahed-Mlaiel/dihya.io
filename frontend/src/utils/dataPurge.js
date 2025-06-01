/**
 * @file dataPurge.js
 * @description Utilitaire de purge de données pour Dihya Coding : efface localement les données sensibles (logs, historiques, tokens), sécurité, conformité RGPD (droit à l’oubli), auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Purge toutes les données locales sensibles (logs, tokens, historiques).
 * @param {object} [options] - { log: bool }
 * @returns {boolean} Succès de la purge
 */
export function purgeAllData(options = {}) {
  if (!hasConsent()) return false;
  try {
    // Liste des clés à purger (à adapter selon l’app)
    const keys = [
      'auth_token',
      'user_profile',
      'monitoring_events',
      'monitoring_service_logs',
      'notification_service_logs',
      'seo_service_logs',
      'voice_service_logs',
      'ecommerce_template_logs',
      'education_template_logs',
      'social_template_logs',
      'generation_service_logs',
      'api_utils_logs',
      'data_export_logs',
      'antiddos_logs',
      'utils_logs',
      // Consentements (optionnel, à ne pas supprimer sans confirmation explicite)
      // 'auth_service_feature_consent', ...
    ];
    keys.forEach(k => window.localStorage.removeItem(k));
    if (options.log !== false) {
      logDataPurgeEvent('purge_all', { timestamp: new Date().toISOString() });
    }
    return true;
  } catch {
    return false;
  }
}

/**
 * Purge une clé spécifique du localStorage.
 * @param {string} key - Nom de la clé à effacer
 * @param {object} [options] - { log: bool }
 * @returns {boolean} Succès de la purge
 */
export function purgeKey(key, options = {}) {
  if (!hasConsent()) return false;
  try {
    window.localStorage.removeItem(sanitizeKey(key));
    if (options.log !== false) {
      logDataPurgeEvent('purge_key', { key: anonymizeKey(key), timestamp: new Date().toISOString() });
    }
    return true;
  } catch {
    return false;
  }
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('data_purge_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logDataPurgeEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('data_purge_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('data_purge_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Sanitize une clé pour éviter l’injection.
 * @param {string} key
 * @returns {string}
 */
function sanitizeKey(key) {
  return String(key).replace(/[^a-zA-Z0-9_\-:.]/g, '').slice(0, 48);
}

/**
 * Anonymise une clé pour les logs.
 * @param {string} key
 * @returns {string}
 */
function anonymizeKey(key) {
  if (!key) return '';
  return key.length > 8 ? key.slice(0, 2) + '***' + key.slice(-2) : '***';
}

/**
 * Efface les logs de purge (droit à l’oubli RGPD).
 */
export function clearLocalDataPurgeLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('data_purge_logs');
  }
}

/* Documentation claire : chaque fonction est commentée pour auditabilité et conformité */