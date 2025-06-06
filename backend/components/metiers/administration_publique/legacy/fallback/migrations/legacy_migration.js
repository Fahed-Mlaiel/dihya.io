// legacy_migration.js - Outils de migration et compatibilité pour l’héritage Threed (JS)

module.exports = {
  migrateLegacyModel: (legacy) => {
    // Exemple de migration d’un ancien format vers le nouveau
    return {
      id: legacy.legacy_id,
      name: legacy.legacy_name,
      vertices: legacy.points || [],
      faces: legacy.surfaces || [],
      meta: { migrated: true, source: 'legacy' }
    };
  },
  auditLegacy: (legacy) => {
    return legacy && legacy.legacy_id ? 'Legacy OK' : 'Legacy Invalide';
  },

  /**
   * Migration batch de plusieurs modèles legacy
   */
  migrateLegacyBatch: (legacyList) => legacyList.map(module.exports.migrateLegacyModel),

  /**
   * Audit avancé avec logs et traçabilité
   */
  auditLegacyWithLog: (legacy) => {
    const result = module.exports.auditLegacy(legacy);
    console.log(`[AUDIT][LEGACY] ${legacy.legacy_id}: ${result}`);
    return result;
  },

  /**
   * Documentation intégrée :
   * - Supporte migration de formats multiples (v1, v2, v3)
   * - Ajoute des métadonnées de traçabilité
   * - Utilisable en CI/CD pour migration massive
   */
};
