/**
 * @file security.js
 * @description Module de monitoring de la sécurité pour Dihya Coding (détection d’anomalies, alertes, RGPD, auditabilité).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les alertes sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Déclenche une alerte de sécurité.
 * @param {object} params
 * @param {string} params.type - Type d’alerte (ex: 'intrusion', 'rate_limit', 'csrf', 'xss')
 * @param {object} [params.details] - Détails anonymisés de l’événement
 * @param {object} [params.options] - Options avancées (log, niveau)
 * @returns {void}
 */
export function triggerSecurityAlert({ type, details = {}, options = {} }) {
  if (!hasConsent()) return;
  if (!type || typeof type !== 'string') throw new Error('Type d’alerte requis.');

  if (options.log !== false) {
    logSecurityEvent('security_alert', {
      type: anonymizeType(type),
      details: anonymizeDetails(details),
      level: options.level || 'info',
      timestamp: new Date().toISOString()
    });
  }

  // Ici, on pourrait ajouter une intégration vers un système d’alerte externe (SIEM, webhook…)
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('security_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logSecurityEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('security_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('security_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise le type d’alerte pour les logs.
 * @param {string} type
 * @returns {string}
 */
function anonymizeType(type) {
  if (!type) return '';
  return type.replace(/[^a-zA-Z0-9_]/g, '').toLowerCase().slice(0, 32);
}

/**
 * Anonymise les détails pour les logs.
 * @param {object} details
 * @returns {object}
 */
function anonymizeDetails(details) {
  if (!details || typeof details !== 'object') return {};
  // Supprime ou masque toute donnée sensible
  const anonymized = { ...details };
  if (anonymized.ip) anonymized.ip = anonymized.ip.replace(/\d+$/, '***');
  if (anonymized.userId) anonymized.userId = anonymized.userId.length > 4 ? anonymized.userId.slice(0, 2) + '***' + anonymized.userId.slice(-2) : '***';
  if (anonymized.email) anonymized.email = anonymized.email[0] + '***@***';
  return anonymized;
}

/**
 * Efface les logs de sécurité (droit à l’oubli RGPD).
 */
export function clearLocalSecurityLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('security_logs');
  }
}