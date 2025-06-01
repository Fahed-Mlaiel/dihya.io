// Point d’entrée JS pour scripts backend Dihya (plugins, CLI, hooks, etc.)

const { runAudit } = require('./audit/main');
const { runBackup } = require('./backup/main');

module.exports = {
  runAudit,
  runBackup,
};
