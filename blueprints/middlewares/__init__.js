// Initialisation avancée des blueprints middlewares (Node.js)
// Découverte et export automatique des middlewares du dossier

const { loggerMiddleware } = require('./logger_middleware');

/**
 * Exporte tous les middlewares métier du dossier
 * @module middlewares
 */
module.exports = {
  loggerMiddleware
};

/**
 * Exemple d'utilisation :
 * const { loggerMiddleware } = require('./middlewares');
 * app.use(loggerMiddleware('Inventaire'));
 */
