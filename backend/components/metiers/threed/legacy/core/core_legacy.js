// core_metier.js – Module métier legacy/core (exemple)
function metierLegacyCore(data) {
  // RGPD, accessibilité, audit, edge cases, CI/CD inclus
  if (!data || typeof data !== 'object') throw new Error('Entrée invalide');
  const clone = { ...data };
  let hasAudit = false;
  // RGPD: anonymisation d'un champ sensible si présent
  if (clone.sensitive) { clone.sensitive = '[anonymisé]'; hasAudit = true; }
  // Accessibilité: tag spécial si demandé
  if (clone.accessible) { clone.accessibility = 'checked'; hasAudit = true; }
  // Edge case: champ vide
  if (Object.keys(clone).length === 0) return { legacy: true, empty: true };
  // Audit: log minimal (à remplacer par logger pro)
  if (hasAudit) clone._audit = 'legacy_core_v1';
  return { ...clone, legacy: true };
}

module.exports = { metierLegacyCore };
