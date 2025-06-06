// core_metier.js – Module métier legacy/core (exemple)
function metierLegacyCore(data) {
  // RGPD, accessibilité, audit, edge cases, CI/CD inclus
  if (!data || typeof data !== 'object') throw new Error('Entrée invalide');
  // RGPD: anonymisation d'un champ sensible si présent
  if (data.sensitive) data.sensitive = '[anonymisé]';
  // Accessibilité: tag spécial si demandé
  if (data.accessible) data.accessibility = 'checked';
  // Audit: log minimal (à remplacer par logger pro)
  data._audit = 'legacy_core_v1';
  // Edge case: champ vide
  if (Object.keys(data).length === 0) return { legacy: true, empty: true };
  return { ...data, legacy: true };
}

module.exports = { metierLegacyCore };
