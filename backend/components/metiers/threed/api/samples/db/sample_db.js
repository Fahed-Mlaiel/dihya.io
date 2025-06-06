/* global console */
// Exemple ultra avancé clé en main du mock DB API Threed (JS)
const db = require('../db/db');
const { auditEntity } = require('../audit/audit');
const { rgpdSanitize } = require('../rgpd/rgpd');
const { checkAccessibility } = require('../accessibility/accessibility');

async function sampleDbUltra() {
  // Création
  const data = { name: 'UltraDB', status: 'active' };
  const created = db.insert('threed', data);
  auditEntity(created, 'create');
  console.info('Création:', created);

  // Lecture
  let entity = db.findById('threed', created.id);
  entity = rgpdSanitize(entity);
  checkAccessibility(entity);
  console.info('Lecture:', entity);

  // Mise à jour
  const updated = db.update('threed', created.id, { status: 'inactive' });
  auditEntity(updated, 'update');
  console.info('Mise à jour:', updated);

  // Suppression
  const deleted = db.delete('threed', created.id);
  auditEntity({ id: created.id }, 'delete');
  console.info('Suppression:', deleted);

  // Edge case
  try {
    db.findById('threed', -1);
  } catch (e) {
    console.warn('Erreur accès:', e);
  }
  console.log('DB ultra avancé exécuté avec succès.');
}

module.exports = { sampleDbUltra };
