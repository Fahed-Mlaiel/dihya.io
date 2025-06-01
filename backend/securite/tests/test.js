// Test d’intégration sécurité Dihya Coding
// RGPD, plugins, audit, accessibilité, CI/CD, monitoring, fallback AI
const assert = require('assert');
const { checkSecurity, checkGDPR, checkPlugins, checkAudit, checkAccessibility, checkCI, checkMonitoring, checkFallbackAI } = require('../../utils/utils');

describe('Sécurité – Dihya Coding', () => {
  it('doit valider toutes les exigences de sécurité avancées', async () => {
    assert(await checkSecurity());
    assert(await checkGDPR());
    assert(await checkPlugins());
    assert(await checkAudit());
    assert(await checkAccessibility());
    assert(await checkCI());
    assert(await checkMonitoring());
    assert(await checkFallbackAI());
  });
});
