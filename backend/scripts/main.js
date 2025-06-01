// Script principal JS pour gestion des scripts backend Dihya

const { runAudit, runBackup } = require('./index');

async function main() {
  await runAudit();
  await runBackup();
}

if (require.main === module) {
  main();
}
