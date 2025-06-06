/* global console */
// Exemple ultra avancé clé en main des middlewares API Threed (JS)
const { auditRequest, rgpdMiddleware, accessibilityMiddleware } = require('../middlewares/middlewares');

function sampleMiddlewaresUltra(app) {
  app.use(rgpdMiddleware);
  app.use(accessibilityMiddleware);
  app.use(auditRequest);
  console.info('Middlewares ultra avancé appliqués');
  console.log('Middlewares ultra avancé exécuté avec succès.');
}

module.exports = { sampleMiddlewaresUltra };
