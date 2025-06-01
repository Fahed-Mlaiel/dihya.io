/**
 * @file monitoringService.js
 * @description Service centralisé de monitoring pour Dihya Coding : suivi des erreurs, incidents, performances, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Enregistre un événement de monitoring (erreur, incident, performance).
 * @param {string} type - Type d’événement ('error', 'incident', 'performance', etc.)
 * @param {object} details - Détails de l’événement (anonymisés)
 * @param {object} [options] - Options avancées (logs, RGPD, etc.)
 * @returns {boolean} Succès de l’enregistrement
 */
export function logMonitoringEvent(type, details = {}, options = {}) {
  if (!hasConsent()) return false;
  const safeType = sanitizeType(type);
  const safeDetails = anonymizeDetails(details);

  try {
    const logs = JSON.parse(window.localStorage.getItem('monitoring_events') || '[]');
    logs.push({
      type: safeType,
      details: safeDetails,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('monitoring_events', JSON.stringify(logs));
    if (options.log !== false) {
      logMonitoringServiceEvent('monitoring_event', { type: safeType, timestamp: new Date().toISOString() });
    }
    return true;
  } catch {
    return false;
  }
}

/**
 * Récupère l’historique local des événements de monitoring.
 * @returns {Array} Liste des événements (anonymisés)
 */
export function getMonitoringHistory() {
  try {
    const logs = JSON.parse(window.localStorage.getItem('monitoring_events') || '[]');
    return logs;
  } catch {
    return [];
  }
}

/**
 * Efface l’historique de monitoring (droit à l’oubli RGPD).
 */
export function clearMonitoringHistory() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('monitoring_events');
  }
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('monitoring_service_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logMonitoringServiceEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('monitoring_service_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('monitoring_service_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Sanitize le type d’événement pour éviter l’injection.
 * @param {string} type
 * @returns {string}
 */
function sanitizeType(type) {
  return String(type).replace(/[^a-zA-Z0-9_\-:.]/g, '').slice(0, 32);
}

/**
 * Anonymise les détails d’un événement pour les logs.
 * @param {object} details
 * @returns {object}
 */
function anonymizeDetails(details) {
  const anonymized = {};
  Object.entries(details || {}).forEach(([k, v]) => {
    if (typeof v === 'string' && k.match(/email|user|ip|token/i)) {
      anonymized[k] = v.length > 4 ? v.slice(0, 2) + '***' + v.slice(-2) : '***';
    } else if (typeof v === 'string' && v.length > 64) {
      anonymized[k] = v.slice(0, 32) + '...';
    } else {
      anonymized[k] = v;
    }
  });
  return anonymized;
}

/**
 * Efface les logs monitoring service (droit à l’oubli RGPD).
 */
export function clearLocalMonitoringServiceLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('monitoring_service_logs');
  }
}