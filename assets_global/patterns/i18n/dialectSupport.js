// dialectSupport.js – Gestion dynamique des variantes/dialectes
// (Exemple métier)

function getDialect(lang, region) {
  // Logique d’aiguillage dialectal
  return `${lang}_${region}`;
}

module.exports = { getDialect };
