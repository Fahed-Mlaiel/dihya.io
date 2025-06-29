// Script d’audit automatique du dossier user
const fs = require('fs');
const path = require('path');

const requiredFiles = [
  'README.md',
  'README_INTEGRATION.md',
  'README_ARCHITECTURE.md',
  'SNIPPETS_EXEMPLES.md',
  'user.mapping.json',
  'user.meta.json',
  'user.tags.json',
  'index.js',
  'DOC_AUTO.md',
  'BADGE_AUDIT.md',
  'AUDIT_REPORT.json',
  'UserProfile.jsx',
  'UserSettings.jsx',
  'UserAvatar.jsx',
  'RGPDPanel.jsx',
  'AuditPanel.jsx'
];

const dir = __dirname;
let missing = [];
for (const file of requiredFiles) {
  if (!fs.existsSync(path.join(dir, file))) {
    missing.push(file);
  }
}
if (missing.length === 0) {
  console.log('Audit user: OK');
} else {
  console.error('Audit user: fichiers manquants:', missing);
  process.exit(1);
}
