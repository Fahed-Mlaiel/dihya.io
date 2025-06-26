// Gestion avancée des locales
module.exports = {
  getLocale: (lang) => require(`./${lang}.json`)
};
