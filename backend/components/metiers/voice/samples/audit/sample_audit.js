/* global console */

// Fonction auditLog attendue par les tests
function auditLog(event) {
  console.log('[AUDIT]', event);
}

// Export par défaut : la fonction auditLog comme fonction principale
module.exports = auditLog;
