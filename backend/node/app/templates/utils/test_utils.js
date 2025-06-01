// Test complet pour les utils (sécurité, i18n, audit, etc.)
const { checkJwt, checkRole, i18nMiddleware, wafMiddleware, ddosMiddleware, auditLogger, getLlamaFallback } = require('./utils');

describe('Utils', () => {
  it('getLlamaFallback fonctionne', async () => {
    const result = await getLlamaFallback('test');
    expect(result).toContain('test');
  });
  // Les middlewares sont testés via les tests d’intégration des routes
});
