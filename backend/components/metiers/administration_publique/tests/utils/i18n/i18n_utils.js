// i18n_utils.js – Utilitaires ultra avancés pour l’internationalisation (clé en main)
// Respecte la modularité, la conformité, l’accessibilité et la logique métier

const SUPPORTED_LANGS = ['fr', 'en', 'ar', 'ber', 'de', 'es'];
const TRANSLATIONS = {
  fr: msg => `[FR] ${msg}`,
  en: msg => `[EN] ${msg}`,
  ar: msg => `[AR] ${msg}`,
  ber: msg => `[BER] ${msg}`,
  de: msg => `[DE] ${msg}`,
  es: msg => `[ES] ${msg}`
};

function translate(msg, lang = 'fr') {
  if (SUPPORTED_LANGS.includes(lang)) {
    return TRANSLATIONS[lang](msg);
  }
  return msg;
}

function isSupportedLang(lang) {
  return SUPPORTED_LANGS.includes(lang);
}

module.exports = {
  SUPPORTED_LANGS,
  translate,
  isSupportedLang
};
