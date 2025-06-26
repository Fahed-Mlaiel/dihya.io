// Legacy audit sample pour mobile
const logger = require('console');

// Fonction principale d'audit attendue par les tests
function auditSample(action, user) {
  const now = new Date();
  const yyyy = now.getFullYear();
  const mm = String(now.getMonth() + 1).padStart(2, '0');
  const dd = String(now.getDate()).padStart(2, '0');
  const timestamp = `${yyyy}-${mm}-${dd}`;
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
