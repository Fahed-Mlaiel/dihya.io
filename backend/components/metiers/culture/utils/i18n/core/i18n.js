// i18n.js – Internationalisation et traduction pour Culture (Node.js)
module.exports = function translate(text, lang = 'fr') {
  const translations = {
    fr: `[FR] ${text}`,
    en: `[EN] ${text}`,
    de: `[DE] ${text}`
  };
  return translations[lang] || text;
};
