const console = require('console');

// Script d’analyse avancée des logs d’audit legacy Juridique (JS)
function analyseAuditLogs(logs) {
  const stats = {};
  logs.forEach(log => {
    stats[log.user] = (stats[log.user] || 0) + 1;
  });
  console.log('Statistiques d’audit :', stats);
}

if (require.main === module) {
  // Exemple d’utilisation
  analyseAuditLogs([
    { user: 'admin', action: 'login' },
    { user: 'user1', action: 'delete' },
    { user: 'admin', action: 'update' }
  ]);
}
