// Script principal d’automatisation Dihya (Node.js)
// Sécurité, RGPD, accessibilité, monitoring, backup, plugins, multilingue, documentation intégrée, CI/CD-ready
const { startMonitoring } = require('./monitoring');
const { scheduleBackup } = require('../backup/backup_service');
const { checkFallback } = require('./ai/ai');

function main() {
  console.info('Démarrage de l’automatisation Dihya (sécurité, RGPD, accessibilité, CI/CD)');
  startMonitoring();
  scheduleBackup();
  checkFallback();
  console.info('Automatisation terminée avec succès.');
}

if (require.main === module) {
  main();
}
