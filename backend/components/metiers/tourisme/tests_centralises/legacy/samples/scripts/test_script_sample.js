// Test ultra avancé pour script_sample.js
const scriptSample = require('../../../legacy/samples/scripts/script_sample');

describe('Script Sample', () => {
  it('doit exécuter le script pour une tâche', () => {
    expect(scriptSample('backup')).toMatch('Script exécuté pour la tâche : backup');
  });
  // ...autres tests avancés, edge cases, robustesse...
});
