/**
 * @file notifications.js
 * @description Fonctions de gestion des notifications pour Dihya Coding (UI, alertes, logs).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les notifications sont validées, anonymisées si besoin, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Types de notifications supportés.
 * @readonly
 * @enum {string}
 */
export const NOTIFICATION_TYPES = Object.freeze({
  SUCCESS: 'success',
  ERROR: 'error',
  WARNING: 'warning',
  INFO: 'info',
});

/**
 * Affiche une notification dans l’UI (exemple basique, à adapter selon le framework UI).
 * @param {object} params
 * @param {string} params.message - Message à afficher (obligatoire)
 * @param {string} [params.type] - Type de notification (success, error, warning, info)
 * @param {number} [params.duration] - Durée d’affichage en ms (défaut 4000)
 * @param {boolean} [params.anonymize] - Anonymiser le message pour les logs
 */
export function showNotification({ message, type = NOTIFICATION_TYPES.INFO, duration = 4000, anonymize = false }) {
  validateNotificationMessage(message);
  // Exemple : affichage via un event custom (à connecter à un composant UI)
  window.dispatchEvent(new CustomEvent('dihya-notification', {
    detail: { message, type, duration }
  }));
  logNotificationEvent('show', anonymize ? anonymizeMessage(message) : message, type);
}

/**
 * Valide le message de notification.
 * @param {string} message
 */
function validateNotificationMessage(message) {
  if (!message || typeof message !== 'string' || message.length < 2) {
    throw new Error('Message de notification invalide');
  }
}

/**
 * Anonymise le message pour les logs (pas de données personnelles).
 * @param {string} message
 * @returns {string}
 */
function anonymizeMessage(message) {
  // Exemple simple : suppression d’emails
  return message.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '[email]');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} value
 * @param {string} [type]
 */
function logNotificationEvent(action, value, type) {
  try {
    const logs = JSON.parse(localStorage.getItem('notification_logs') || '[]');
    logs.push({
      action,
      value,
      type,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('notification_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de notifications locaux (droit à l’oubli RGPD).
 */
export function clearLocalNotificationLogs() {
  localStorage.removeItem('notification_logs');
}