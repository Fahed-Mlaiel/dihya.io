/* global console */
// sample_advanced_usage.js – Exemple ultra avancé d'usage métier (API Threed)
const { getById, create } = require('../controllers/threed_controller');
const db = require('../db/db');
const { rgpdSanitize } = require('../rgpd/rgpd');
const { auditEntity } = require('../audit/audit');

function sampleAdvancedUsageUltra() {
  // Création et audit
  const data = { name: 'Advanced', status: 'active', label: 'Demo' };
  const created = create(data);
  auditEntity(created, 'create');
  console.info('Création avancée:', created);
  // Lecture, RGPD, edge case
  let entity = getById(created.id);
  entity = rgpdSanitize(entity);
  console.info('Lecture RGPD:', entity);
  // Insertion DB directe
  const dbEntity = db.insert('threed', { name: 'DBDirect', status: 'test' });
  console.info('DB direct:', dbEntity);
  console.log('Sample advanced usage ultra avancé exécuté avec succès.');
}

module.exports = sampleAdvancedUsageUltra;
