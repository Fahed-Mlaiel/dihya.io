// Script de backup automatique des composants molecules
const fs = require('fs');
const path = require('path');

const MOLECULES_DIR = path.join(__dirname, '../src/components/molecules');
const BACKUP_DIR = path.join(__dirname, 'backups', `molecules_${Date.now()}`);

function backupMolecules() {
  fs.mkdirSync(BACKUP_DIR, { recursive: true });
  fs.readdirSync(MOLECULES_DIR).forEach(file => {
    if (file.endsWith('.jsx') || file.startsWith('README')) {
      fs.copyFileSync(
        path.join(MOLECULES_DIR, file),
        path.join(BACKUP_DIR, file)
      );
    }
  });
  console.log('Backup terminé dans', BACKUP_DIR);
}

backupMolecules();
