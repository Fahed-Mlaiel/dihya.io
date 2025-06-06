/* global console */
// Exemple ultra avancé clé en main des hooks API Threed (JS)
const { beforeAction, afterAction } = require('../hooks/hooks');
const { auditEntity } = require('../audit/audit');

async function sampleHooksUltra() {
  beforeAction('read', { id: 1 });
  console.info('Avant lecture');
  // ... logique métier ...
  auditEntity({ id: 1 }, 'read');
  afterAction('read', { id: 1 });
  console.info('Après lecture');
  console.log('Hooks ultra avancé exécuté avec succès.');
}

module.exports = { sampleHooksUltra };
