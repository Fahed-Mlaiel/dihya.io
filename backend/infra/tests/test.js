// Test d’intégration infrastructure Dihya Coding
// Sécurité, monitoring, backup, CI/CD, accessibilité, audit, multilingue
const assert = require('assert');
const { checkSecurity, checkMonitoring, checkBackup, checkCI, checkAccessibility, checkI18n } = require('../../utils/utils');

describe('Infrastructure – Sécurité & Conformité', () => {
  it('doit valider toutes les exigences critiques', async () => {
    assert(await checkSecurity());
    assert(await checkMonitoring());
    assert(await checkBackup());
    assert(await checkCI());
    assert(await checkAccessibility());
    assert(await checkI18n(['fr','en','ar','de','es','it','pt','ru','zh','ja','tr','ber','nl']));
  });
});
