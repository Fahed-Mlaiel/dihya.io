/* global console */
// Exemple ultra avancé clé en main du module RGPD API Threed (JS)
const { rgpdSanitize } = require('../rgpd/rgpd');
const { auditEntity } = require('../audit/audit');

function sampleRgpdUltra() {
  const entity = { name: 'Test', email: 'test@dihya.io' };
  const sanitized = rgpdSanitize(entity);
  auditEntity(sanitized, 'rgpdSanitize');
  console.info('Sanitized:', sanitized);
  // Edge case: données déjà anonymisées
  const sanitized2 = rgpdSanitize({ name: null, email: null });
  console.info('Sanitized edge:', sanitized2);
  console.log('RGPD ultra avancé exécuté avec succès.');
}

module.exports = { sampleRgpdUltra };
