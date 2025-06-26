// rollback.js
// Script de rollback automatisé (Lead Dev)
// Permet de restaurer un état antérieur des composants critiques du frontend

const fs = require('fs');
const path = require('path');

const BACKUP_DIR = path.join(__dirname, 'backups');
const TARGET_DIR = path.join(__dirname, '../components');

function restoreBackup(component) {
  const backupPath = path.join(BACKUP_DIR, `${component}.bak`);
  const targetPath = path.join(TARGET_DIR, component);
  if (fs.existsSync(backupPath)) {
    fs.copyFileSync(backupPath, targetPath);
    console.log(`✅ ${component} restauré depuis la sauvegarde.`);
  } else {
    console.error(`❌ Sauvegarde introuvable pour ${component}`);
  }
}

// Exemple d’utilisation : node rollback.js atoms.js
const component = process.argv[2];
if (!component) {
  console.error('Usage : node rollback.js <component>');
  process.exit(1);
}
restoreBackup(component);

module.exports = { rollback };
