// Script de backup automatique de tous les components
const fs = require('fs');
const path = require('path');

const COMPONENTS_DIR = path.join(__dirname, '../src/components');
const BACKUP_DIR = path.join(__dirname, 'backups', `components_${Date.now()}`);
const SUBFOLDERS = ['atoms', 'molecules', 'organisms', 'templates'];

function backupComponents() {
  fs.mkdirSync(BACKUP_DIR, { recursive: true });
  SUBFOLDERS.forEach(sub => {
    const dir = path.join(COMPONENTS_DIR, sub);
    if (fs.existsSync(dir)) {
      fs.readdirSync(dir).forEach(file => {
        if (file.endsWith('.jsx') || file.startsWith('README')) {
          fs.copyFileSync(
            path.join(dir, file),
            path.join(BACKUP_DIR, `${sub}_${file}`)
          );
        }
      });
    }
  });
  console.log('Backup terminé dans', BACKUP_DIR);
}

backupComponents();

module.exports = { backup_components };
