/**
 * @file trackEvent.js
 * @description Fonction centralisée pour le tracking d’événements sur Dihya Coding.
 * Respecte la RGPD, la sécurité, l’auditabilité et l’extensibilité.
 * Compatible multi-plugins (Matomo, Plausible, etc.).
 * Ne collecte aucune donnée personnelle sans consentement explicite.
 */

/**
 * Valide la structure d’un événement analytics.
 * @param {Object} event - L’événement à valider.
 * @returns {boolean} true si valide, false sinon.
 */
function validateEvent(event) {
  if (!event || typeof event !== 'object') return false;
  if (!event.name || typeof event.name !== 'string') return false;
  if (event.data && typeof event.data !== 'object') return false;
  return true;
}

/**
 * Envoie l’événement à tous les plugins analytics actifs.
 * @param {Object} event - { name: string, data?: object }
 * @param {Object} [options] - { anonymize?: boolean }
 * @returns {Promise<void>}
 */
export async function trackEvent(event, options = {}) {
  // Vérification du consentement utilisateur (RGPD)
  if (!window?.localStorage?.getItem('analytics_consent')) return;

  // Validation de l’événement
  if (!validateEvent(event)) {
    if (process.env.NODE_ENV === 'development') {
      console.warn('[Analytics] Événement invalide', event);
    }
    return;
  }

  // Anonymisation si demandé
  const eventData = options.anonymize
    ? anonymizeData(event.data)
    : event.data;

  // Audit log local (pour auditabilité)
  logEventLocally({ ...event, data: eventData });

  // Envoi vers chaque plugin configuré
  if (window._matomo) {
    window._matomo.push(['trackEvent', event.name, JSON.stringify(eventData || {})]);
  }
  if (window.plausible) {
    window.plausible(event.name, { props: eventData });
  }
  // Ajouter ici d’autres intégrations analytics si besoin
}

/**
 * Anonymise les données d’événement (aucune donnée personnelle).
 * @param {Object} data
 * @returns {Object}
 */
function anonymizeData(data) {
  if (!data) return {};
  // Exemple simple : supprimer les champs potentiellement sensibles
  const { email, userId, ...rest } = data;
  return rest;
}

/**
 * Log local pour auditabilité (non envoyé à un serveur).
 * @param {Object} event
 */
function logEventLocally(event) {
  try {
    const logs = JSON.parse(localStorage.getItem('analytics_logs') || '[]');
    logs.push({ ...event, timestamp: new Date().toISOString() });
    localStorage.setItem('analytics_logs', JSON.stringify(logs));
  } catch (e) {
    // Silencieux pour éviter tout blocage UX
  }
}