// Legacy audit sample pour threed
const logger = require('console');

// Fonction principale d'audit attendue par les tests
function auditSample(action, user) {
  const timestamp = new Date().toISOString().split('T')[0]; // Format YYYY-MM-DD
  return `[AUDIT] ${action} by ${user} @ ${timestamp}`;
}

// Fonction basique pour éviter les erreurs
function basicFunction() {
  return { success: true, module: 'audit_sample' };
}

// Classe basique pour les modules qui en ont besoin
class BasicClass {
  constructor(options = {}) {
    this.options = options;
  }

  init() {
    return true;
  }

  process(data) {
    return { success: true, data };
  }
}

// Export par défaut : la fonction auditSample comme fonction principale
module.exports = auditSample;
