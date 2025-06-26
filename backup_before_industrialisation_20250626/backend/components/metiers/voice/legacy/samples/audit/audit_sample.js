// Legacy audit sample pour voice

// Fonction principale d'audit attendue par les tests
function auditSample(action, user) {
  const now = new Date();
  const yyyy = now.getFullYear();
  const mm = String(now.getMonth() + 1).padStart(2, '0');
  const dd = String(now.getDate()).padStart(2, '0');
  const timestamp = `${yyyy}-${mm}-${dd}`;
  return `[AUDIT] ${action} by ${user} @ ${timestamp}`;
}

// Export par défaut : la fonction auditSample comme fonction principale
module.exports = auditSample;
