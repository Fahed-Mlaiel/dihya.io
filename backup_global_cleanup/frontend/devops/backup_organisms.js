// Script de backup automatique des composants organisms
const fs = require('fs');
const path = require('path');

const ORGANISMS_DIR = path.join(__dirname, '../src/components/organisms');
const BACKUP_DIR = path.join(__dirname, 'backups', `organisms_${Date.now()}`);

function backupOrganisms() {
  fs.mkdirSync(BACKUP_DIR, { recursive: true });
  fs.readdirSync(ORGANISMS_DIR).forEach(file => {
    if (file.endsWith('.jsx') || file.startsWith('README')) {
      fs.copyFileSync(
        path.join(ORGANISMS_DIR, file),
        path.join(BACKUP_DIR, file)
      );
    }
  });
  console.log('Backup terminé dans', BACKUP_DIR);
}

backupOrganisms();
