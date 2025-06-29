// Script d’audit automatique du dossier plugins
const fs = require('fs');
const path = require('path');

const requiredFiles = [
  'README.md',
  'README_INTEGRATION.md',
  'README_ARCHITECTURE.md',
  'SNIPPETS_EXEMPLES.md',
  'plugins.mapping.json',
  'plugins.meta.json',
  'plugins.tags.json',
  'index.js',
  'DOC_AUTO.md',
  'BADGE_AUDIT.md',
  'AUDIT_REPORT.json',
  'PluginManager.jsx',
  'PluginInstaller.jsx'
];

const dir = __dirname;
let missing = [];
for (const file of requiredFiles) {
  if (!fs.existsSync(path.join(dir, file))) {
    missing.push(file);
  }
}
if (missing.length === 0) {
  console.log('Audit plugins: OK');
} else {
  console.error('Audit plugins: fichiers manquants:', missing);
  process.exit(1);
}
