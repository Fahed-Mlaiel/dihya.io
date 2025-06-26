// Script de backup automatique des composants templates
const fs = require('fs');
const path = require('path');

const TEMPLATES_DIR = path.join(__dirname, '../src/components/templates');
const BACKUP_DIR = path.join(__dirname, 'backups', `templates_${Date.now()}`);

function backupTemplates() {
  fs.mkdirSync(BACKUP_DIR, { recursive: true });
  fs.readdirSync(TEMPLATES_DIR).forEach(file => {
    if (file.endsWith('.jsx') || file.startsWith('README')) {
      fs.copyFileSync(
        path.join(TEMPLATES_DIR, file),
        path.join(BACKUP_DIR, file)
      );
    }
  });
  console.log('Backup terminé dans', BACKUP_DIR);
}

backupTemplates();

module.exports = { backup_templates };
