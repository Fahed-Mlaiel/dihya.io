// Utils.js – Zentrale Hilfsfunktionen für Frontend/Backend

/**
 * Validiert eine E-Mail-Adresse (RGPD-konform)
 */
export function validateEmail(email) {
  return /^[\w.-]+@[\w.-]+\.\w+$/.test(email);
}

/**
 * Strukturiertes Logging (Audit, SEO, Plugins)
 */
export function structuredLog(event, data = {}) {
  // In Produktion: Logging-Backend anbinden
  console.info(`[LOG] ${event}`, data);
}

/**
 * Mehrsprachige Nachricht (i18n)
 */
export function i18nMessage(key, lang = 'en') {
  // Dummy: In Produktion mit i18n-Bibliothek
  return key;
}

// Weitere Hilfsfunktionen: Audit, Security, Serialisierung, Plugins...
