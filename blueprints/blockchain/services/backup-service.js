// Service de sauvegarde/restauration des données
const fs = require('fs');
const path = require('path');
const BACKUP_PATH = process.env.BACKUP_PATH || path.join(__dirname, '../../backups/data.bak');

module.exports = {
  backup(data) {
    if (!data) throw new Error('Aucune donnée à sauvegarder');
    fs.writeFileSync(BACKUP_PATH, JSON.stringify(data));
    console.log('[BACKUP] Sauvegarde réussie:', BACKUP_PATH);
  },
  restore() {
    if (!fs.existsSync(BACKUP_PATH)) throw new Error('Aucune sauvegarde trouvée');
    const raw = fs.readFileSync(BACKUP_PATH);
    console.log('[BACKUP] Restauration réussie');
    return JSON.parse(raw);
  }
};

module.exports.BackupService = module.exports;
