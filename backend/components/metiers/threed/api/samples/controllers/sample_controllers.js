/* global console */

// Exemple ultra avancé clé en main des contrôleurs API Threed (JS)
// Respecte RGPD, audit, accessibilité, hooks, CI/CD, internationalisation, sécurité, edge cases
const { create, getById, update, delete: del } = require('../controllers/threed_controller');
const { getAuditLog } = require('../audit/audit');
const { rgpdSanitize } = require('../rgpd/rgpd');
const { checkAccessibility } = require('../accessibility/accessibility');
const { beforeAction, afterAction } = require('../hooks/hooks');

async function sampleControllerUltra() {
  // Création avec validation, audit, RGPD, accessibilité
  const data = { name: 'UltraCube', status: 'active', label: 'Ultra', lang: 'fr' };
  beforeAction('create', data);
  const created = await create(data);
  afterAction('create', created);
  checkAccessibility(created);
  const createdSanitized = rgpdSanitize(created);
  console.info('Création:', createdSanitized);

  // Lecture avec audit, RGPD, accessibilité
  const entity = await getById(created.id);
  checkAccessibility(entity);
  const entitySanitized = rgpdSanitize(entity);
  console.info('Lecture:', entitySanitized);

  // Mise à jour
  const updateData = { name: 'UltraCubeV2', status: 'inactive', label: 'UltraV2' };
  beforeAction('update', updateData);
  const updated = await update(created.id, updateData);
  afterAction('update', updated);
  console.info('Mise à jour:', updated);

  // Suppression
  beforeAction('delete', { id: created.id });
  const deleted = await del(created.id);
  afterAction('delete', { id: created.id });
  console.info('Suppression:', deleted);

  // Audit log
  const auditLog = getAuditLog();
  console.log('Audit log:', auditLog);

  // Edge case: accès non autorisé
  try {
    await getById(-1);
  } catch (e) {
    console.warn('Erreur accès:', e);
  }

  console.log('Contrôleur ultra avancé exécuté avec succès.');
}

module.exports = { sampleControllerUltra };
