/**
 * Template utilitaire pour la génération de routes, middlewares et sécurité avancée.
 * Fournit : checkJwt, checkRole, i18nMiddleware, wafMiddleware, ddosMiddleware, auditLogger, getLlamaFallback
 * Multilingue, RGPD, plugins, SEO, tests, CI/CD, Docker, K8s ready.
 */

const {
  checkJwt,
  checkRole,
  i18nMiddleware,
  wafMiddleware,
  ddosMiddleware,
  auditLogger,
  getLlamaFallback
} = require('./utils');

module.exports = {
  checkJwt,
  checkRole,
  i18nMiddleware,
  wafMiddleware,
  ddosMiddleware,
  auditLogger,
  getLlamaFallback
};
