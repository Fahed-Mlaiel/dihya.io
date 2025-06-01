/**
 * @file analytics.js
 * @description API centralisée pour la gestion des analytics côté frontend Dihya Coding.
 * Respecte la RGPD, la sécurité, l’auditabilité et l’extensibilité.
 * Toutes les requêtes sont validées, anonymisées et loguées localement pour audit.
 * Ne jamais exposer de données personnelles sans consentement explicite.
 */

import { trackEvent } from '../analytics/trackEvent';

/**
 * Envoie un événement analytics métier à la couche tracking.
 * @param {string} name - Nom de l’événement (ex: 'project_generated')
 * @param {object} [data] - Données additionnelles anonymisées
 * @param {object} [options] - Options (ex: { anonymize: true })
 * @returns {Promise<void>}
 * @example
 *   sendAnalytics('project_generated', { projectType: 'web' });
 */
export async function sendAnalytics(name, data = {}, options = {}) {
  if (!name || typeof name !== 'string') {
    if (process.env.NODE_ENV === 'development') {
      console.warn('[Analytics API] Nom d’événement invalide', name);
    }
    return;
  }
  await trackEvent({ name, data }, options);
}

/**
 * Récupère les logs analytics locaux pour auditabilité.
 * @returns {Array<Object>} Liste des événements trackés localement
 */
export function getLocalAnalyticsLogs() {
  try {
    return JSON.parse(localStorage.getItem('analytics_logs') || '[]');
  } catch {
    return [];
  }
}

/**
 * Efface les logs analytics locaux (conformité RGPD, droit à l’oubli).
 */
export function clearLocalAnalyticsLogs() {
  localStorage.removeItem('analytics_logs');
}