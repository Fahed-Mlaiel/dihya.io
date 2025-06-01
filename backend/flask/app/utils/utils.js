// utils.js – Fonctions utilitaires (validation, logging, i18n, audit, RGPD, plugins)

/**
 * Valide un email (RGPD)
 */
function validateEmail(email) {
  return /^[\w.-]+@[\w.-]+\.\w+$/.test(email);
}

/**
 * Log structuré (audit, SEO, plugins)
 */
function structuredLog(event, data = {}) {
  console.info(`[LOG] ${event}`, data);
}

/**
 * Message i18n (dummy)
 */
function i18nMessage(key, lang = 'fr') {
  return key;
}

module.exports = {
  validateEmail,
  structuredLog,
  i18nMessage,
  // ...autres utilitaires RGPD, plugins...
};
