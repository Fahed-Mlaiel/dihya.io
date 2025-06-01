/**
 * @file analyticsService.js
 * @description Service centralisé d’analytics pour Dihya Coding : suivi des événements, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Enregistre un événement analytics de façon sécurisée et conforme RGPD.
 * @param {string} event - Nom de l’événement (ex: 'page_view', 'button_click')
 * @param {object} [data] - Données associées à l’événement (anonymisées)
 * @param {object} [options] - Options avancées (logs, RGPD, etc.)
 * @returns {boolean} Succès de l’enregistrement
 */
export function trackEvent(event, data = {}, options = {}) {
  if (!hasConsent()) return false;
  const safeEvent = sanitizeEventName(event);
  const safeData = anonymizeEventData(data);

  try {
    const logs = JSON.parse(window.localStorage.getItem('analytics_events') || '[]');
    logs.push({
      event: safeEvent,
      data: safeData,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('analytics_events', JSON.stringify(logs));
    if (options.log !== false) {
      logAnalyticsServiceEvent('track_event', { event: safeEvent, timestamp: new Date().toISOString() });
    }
    return true;
  } catch {
    return false;
  }
}

/**
 * Récupère l’historique local des événements analytics.
 * @returns {Array} Liste des événements (anonymisés)
 */
export function getAnalyticsHistory() {
  try {
    const logs = JSON.parse(window.localStorage.getItem('analytics_events') || '[]');
    return logs;
  } catch {
    return [];
  }
}

/**
 * Efface l’historique analytics (droit à l’oubli RGPD).
 */
export function clearAnalyticsHistory() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('analytics_events');
  }
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('analytics_service_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logAnalyticsServiceEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('analytics_service_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('analytics_service_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Sanitize le nom d’événement pour éviter l’injection.
 * @param {string} event
 * @returns {string}
 */
function sanitizeEventName(event) {
  return String(event).replace(/[^a-zA-Z0-9_\-:.]/g, '').slice(0, 48);
}

/**
 * Anonymise les données d’événement pour les logs.
 * @param {object} data
 * @returns {object}
 */
function anonymizeEventData(data) {
  const anonymized = {};
  Object.entries(data || {}).forEach(([k, v]) => {
    if (typeof v === 'string' && k.match(/email|user|ip/i)) {
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
 * Efface les logs analytics service (droit à l’oubli RGPD).
 */
export function clearLocalAnalyticsServiceLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('analytics_service_logs');
  }
}