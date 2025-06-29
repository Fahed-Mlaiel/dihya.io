// fallback.js
// Fallback i18n JS pour Crypto – exemple clé en main

/**
 * Retourne une traduction par défaut si la clé n'est pas trouvée
 * @param {string} key
 * @param {object} translations
 * @param {string} defaultValue
 * @returns {string}
 */
function i18nFallback(key, translations, defaultValue = 'N/A') {
  return translations[key] || defaultValue;
}

module.exports = { i18nFallback };
