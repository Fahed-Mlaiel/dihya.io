// Script d’audit automatique du dossier i18n
const fs = require('fs');
const path = require('path');

const requiredFiles = [
  'README.md',
  'README_ARCHITECTURE.md',
  'SNIPPETS_EXEMPLES.md',
  'i18n.mapping.json',
  'i18n.meta.json',
  'i18n.tags.json',
  'index.js',
  'DOC_AUTO.md',
  'BADGE_AUDIT.md',
  'AUDIT_REPORT.json',
  'i18n.js',
  'autoTranslate.js',
  'dialectSupport.js',
  'localeUtils.js',
  'locales'
];

const dir = __dirname;
let missing = [];
for (const file of requiredFiles) {
  if (!fs.existsSync(path.join(dir, file))) {
    missing.push(file);
  }
}
if (missing.length === 0) {
  console.log('Audit i18n: OK');
} else {
  console.error('Audit i18n: fichiers manquants:', missing);
  process.exit(1);
}
