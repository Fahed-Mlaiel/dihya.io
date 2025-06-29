// i18n.js – Module d’accès centralisé aux traductions
// (Exemple métier)

const fs = require('fs');
const path = require('path');

function loadI18n(lang) {
  const file = path.join(__dirname, `i18n_${lang}.json`);
  if (fs.existsSync(file)) {
    return JSON.parse(fs.readFileSync(file, 'utf-8'));
  }
  return {};
}

module.exports = { loadI18n };
