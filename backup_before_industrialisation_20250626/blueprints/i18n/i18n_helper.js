// Blueprint i18n helper métier (Node.js)
// Exemple de fonction de traduction, instructions d’extension

const translations = {
  fr: { titre: 'Gestion des assets' },
  en: { titre: 'Asset Management' },
};

function translate(key, lang = 'fr') {
  const dict = { fr: { hello: 'Bonjour', titre: 'Gestion des assets' }, en: { hello: 'Hello', titre: 'Asset Management' } };
  return dict[lang] && dict[lang][key] ? dict[lang][key] : key;
}

module.exports = { translate };
