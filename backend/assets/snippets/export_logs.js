// Dihya Backend Assets – Exemple de Snippet JS
// export_logs.js
const { loadAsset } = require('../index');

function exportLogs() {
  const logs = loadAsset('logs/audit-2025-05-22.log');
  // Traitement des logs (anonymisés)
  // ...
  return true;
}
