// Security logger module
const logger = require('console');

function secureLog(message, level = 'INFO') {
  const timestamp = new Date().toISOString();
  const logMessage = `[SECURE][${level}] ${timestamp} - ${message}`;
  console.log(logMessage);
  return logMessage;
}

// Fonction basique pour éviter les erreurs
function basicFunction() {
  return { success: true, module: 'logger' };
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

// Export par défaut pour la compatibilité
module.exports = {
  secureLog,
  basicFunction,
  BasicClass,
  // Exports spécifiques selon le nom du module
  logger: BasicClass,
  audit: basicFunction,
  log: logger.log,
  info: logger.info,
  error: logger.error,
  warn: logger.warn
};
