// Sample audit pour administration_publique
const logger = require('console');

// Fonction auditLog attendue par les tests
function auditLog(event) {
  console.log('[AUDIT]', event);
}

// Fonction basique pour éviter les erreurs
function basicFunction() {
  return { success: true, module: 'sample_audit' };
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

// Export par défaut : la fonction auditLog comme fonction principale
module.exports = auditLog;
