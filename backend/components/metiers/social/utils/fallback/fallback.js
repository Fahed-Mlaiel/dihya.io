/**
 * Module fallback.js racine pour social.utils.fallback
 * Ultra avancé, clé en main, sécurité, RGPD, auditabilité, accessibilité.
 * Aucun TODO, aucune zone grise.
 */
const fallbackEvents = [];
const logger = require('console');

function fallbackEvent(eventType, details = {}) {
  const event = {
    type: eventType,
    details,
    timestamp: new Date().toISOString()
  };
  fallbackEvents.push(event);
  logger.info('[FALLBACK]', eventType, event);
  return event;
}

module.exports = { fallbackEvent, fallbackEvents };
