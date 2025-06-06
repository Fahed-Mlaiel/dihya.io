// Point d'entrée du module middlewares

const { auditRequest, rgpdMiddleware, accessibilityMiddleware } = require('./middlewares.js');
module.exports = { auditRequest, rgpdMiddleware, accessibilityMiddleware };
