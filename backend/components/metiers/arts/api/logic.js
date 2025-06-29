/**
 * Helpers et logique métier JS pour le module arts (audit, accessibilité, RGPD, etc.)
 * Utilisez ces fonctions dans tous les contrôleurs API pour garantir la conformité et la traçabilité.
 */

export function auditAccess(user, action, resource) {
  if (!user || !action || !resource) {
    console.info(`[AUDIT] User= Action= Resource=`);
    return;
  }
  console.info(`[AUDIT] User=${user} Action=${action} Resource=${resource}`);
}

export function anonymizeData(data) {
  // RGPD : anonymisation des champs sensibles
  const out = {};
  for (const k in data) out[k] = (k === 'email' || k === 'name') ? '***' : data[k];
  return out;
}

export function isAccessible(entity) {
  // Vérification accessibilité (exemple WCAG/ARIA)
  return entity && (entity.label || entity.alt);
}
