/* global console */
// sample_edge_cases.js – Exemple ultra avancé de gestion des edge cases (API Threed)
const { getById } = require('../controllers/threed_controller');

function sampleEdgeCasesUltra() {
  // Edge case : accès à un ID inexistant
  try {
    const entity = getById(-999);
    if (entity === null || entity === undefined) {
      console.info('Edge case: accès à un ID inexistant OK');
    } else {
      throw new Error('L’ID inexistant retourne une entité !');
    }
  } catch (e) {
    console.warn('Erreur edge case:', e);
  }
  console.log('Sample edge cases ultra avancé exécuté avec succès.');
}

module.exports = sampleEdgeCasesUltra;
