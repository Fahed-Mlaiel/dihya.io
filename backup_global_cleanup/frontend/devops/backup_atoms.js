// Script de backup automatique des composants atoms
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const ATOMS_DIR = path.join(__dirname, '../src/components/atoms');
const BACKUP_DIR = path.join(__dirname, 'backups', `atoms_${Date.now()}`);

function backupAtoms() {
  fs.mkdirSync(BACKUP_DIR, { recursive: true });
  fs.readdirSync(ATOMS_DIR).forEach(file => {
    if (file.endsWith('.jsx') || file.startsWith('README')) {
      fs.copyFileSync(
        path.join(ATOMS_DIR, file),
        path.join(BACKUP_DIR, file)
      );
    }
  });
  console.log('Backup terminé dans', BACKUP_DIR);
}

backupAtoms();
