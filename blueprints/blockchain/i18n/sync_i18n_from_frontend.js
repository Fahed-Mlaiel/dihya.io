// Script Lead Dev : Synchronisation complète des fichiers i18n/locales depuis frontend vers blockchain
// Usage : node sync_i18n_from_frontend.js

const fs = require('fs');
const path = require('path');

const SRC = path.resolve(__dirname, '../../../frontend/src/i18n/locales');
const DEST = path.resolve(__dirname, './locales');

function syncLocales() {
  if (!fs.existsSync(SRC)) {
    console.error('Dossier source introuvable:', SRC);
    return;
  }
  if (!fs.existsSync(DEST)) fs.mkdirSync(DEST, { recursive: true });
  const files = fs.readdirSync(SRC);
  files.forEach(file => {
    const srcFile = path.join(SRC, file);
    const destFile = path.join(DEST, file);
    if (fs.statSync(srcFile).isFile()) {
      fs.copyFileSync(srcFile, destFile);
      console.log('Synchronisé :', file);
    }
  });
  console.log('Synchronisation i18n terminée.');
}

syncLocales();

module.exports = { sync_i18n_from_frontend };
