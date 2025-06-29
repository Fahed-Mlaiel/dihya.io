// Script d’audit automatique du dossier hooks
const fs = require('fs');
const path = require('path');

const requiredFiles = [
  'README.md',
  'README_ARCHITECTURE.md',
  'SNIPPETS_EXEMPLES.md',
  'hooks.mapping.json',
  'hooks.meta.json',
  'hooks.tags.json',
  'index.js',
  'DOC_AUTO.md',
  'BADGE_AUDIT.md',
  'AUDIT_REPORT.json',
  'useAuth.js',
  'useTheme.js',
  'useTranslation.js',
  'useVoiceInput.js',
  'useMarketplace.js',
  'useNotification.js',
  'useAnalytics.js',
  'useModal.js',
  'useMonitoring.js',
  'useCollaborativeEdit.js',
  'usePluginManager.js',
  'useRGPD.js',
  'useLogs.js',
  'useOnboarding.js'
];

const dir = __dirname;
let missing = [];
for (const file of requiredFiles) {
  if (!fs.existsSync(path.join(dir, file))) {
    missing.push(file);
  }
}
if (missing.length === 0) {
  console.log('Audit hooks: OK');
} else {
  console.error('Audit hooks: fichiers manquants:', missing);
  process.exit(1);
}
