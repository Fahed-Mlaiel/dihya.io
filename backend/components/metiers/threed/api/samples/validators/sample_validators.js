/* global console */
// Exemple ultra avancé clé en main des validateurs API Threed (JS)
const { validate3dEntity } = require('../validators/validators');
const { auditEntity } = require('../audit/audit');

function sampleValidatorsUltra() {
  // Validation standard
  validate3dEntity({ name: 'Test', status: 'active' });
  auditEntity({ name: 'Test' }, 'validate');
  console.info('Validation standard OK');
  // Edge case: entité incomplète
  try {
    validate3dEntity({ status: 'active' });
  } catch (e) {
    console.warn('Validation échouée:', e);
  }
  console.log('Validateurs ultra avancé exécuté avec succès.');
}

module.exports = { sampleValidatorsUltra };
