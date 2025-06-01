/**
 * @file analyticsPlugin.js
 * @description Plugin d’analytics pour Dihya Coding : suivi d’événements, UX, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les mesures sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Initialise le plugin analytics.
 * @param {object} [options]
 * @param {boolean} [options.log=true] - Active le log local pour auditabilité
 * @param {function} [options.onEvent] - Callback personnalisé pour chaque événement tracké
 */
export function initAnalyticsPlugin(options = {}) {
  if (!hasConsent()) return;
  // Exemple : écoute des événements de navigation
  if (typeof window !== 'undefined') {
    window.addEventListener('hashchange', () => {
      trackEvent('navigation', { path: window.location.hash }, options);
    });
    window.addEventListener('popstate', () => {
      trackEvent('navigation', { path: window.location.pathname }, options);
    });
  }
}

/**
 * Tracke un événement analytics.
 * @param {string} event - Nom de l’événement (ex: 'page_view', 'click')
 * @param {object} data - Données associées (anonymisées)
 * @param {object} [options]
 */
export function trackEvent(event, data = {}, options = {}) {
  if (!hasConsent()) return;
  const anonymizedData = anonymizeAnalyticsData(data);
  if (options.log !== false) {
    logAnalyticsEvent(event, anonymizedData);
  }
  if (typeof options.onEvent === 'function') {
    options.onEvent({ event, ...anonymizedData });
  }
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('analytics_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} event
 * @param {object} data
 */
function logAnalyticsEvent(event, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('analytics_logs') || '[]');
    logs.push({
      event,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('analytics_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise les données analytics pour les logs.
 * @param {object} data
 * @returns {object}
 */
function anonymizeAnalyticsData(data) {
  const anonymized = { ...data };
  if (anonymized.userId) anonymized.userId = anonymized.userId.length > 4 ? anonymized.userId.slice(0, 2) + '***' + anonymized.userId.slice(-2) : '***';
  if (anonymized.email) anonymized.email = anonymized.email[0] + '***@***';
  if (anonymized.path) anonymized.path = anonymized.path.replace(/\/[a-zA-Z0-9]{24,}/g, '/***');
  return anonymized;
}

/**
 * Efface les logs analytics (droit à l’oubli RGPD).
 */
export function clearLocalAnalyticsLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('analytics_logs');
  }
}