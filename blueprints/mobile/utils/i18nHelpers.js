// i18nHelpers.js
// Helpers avancés pour l’internationalisation (traduction, détection, formatage)

/**
 * Détecte la langue du navigateur
 * @returns {string}
 */
export function detectBrowserLanguage() {
  return navigator.language || navigator.userLanguage || 'fr';
}

/**
 * Traduit une clé selon un dictionnaire fourni
 * @param {string} key
 * @param {Object} dict
 * @param {string} [lang='fr']
 * @returns {string}
 */
export function t(key, dict, lang = 'fr') {
  return (dict[lang] && dict[lang][key]) || key;
}
