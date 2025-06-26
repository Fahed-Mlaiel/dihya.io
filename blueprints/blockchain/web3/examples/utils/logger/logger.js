// Logger avancé pour les scripts blockchain, gestion multi-niveaux, formatage, etc.
const { createLogger, format, transports } = require('winston');

function getLogger(name) {
  return createLogger({
    level: 'info',
    format: format.combine(
      format.label({ label: name }),
      format.timestamp(),
      format.printf(({ timestamp, level, message, label }) => {
        return `[${timestamp}] ${level} ${label}: ${message}`;
      })
    ),
    transports: [new transports.Console()]
  });
}

// Ajoutez ici d'autres loggers ou transports avancés
module.exports = { getLogger };
