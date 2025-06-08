// legacy_helper.js - Fonctions utilitaires avancées pour la gestion de l’héritage Threed (JS)

module.exports = {
  isLegacyModel: (obj) => !!obj.legacy_id,
  convertAll: (legacyList) => legacyList.map(l => ({ ...l, migrated: true })),
  validateLegacy: (legacy) => legacy && typeof legacy.legacy_id === 'string',

  /**
   * Conversion avancée de legacy vers nouveau format avec mapping dynamique
   */
  convertLegacyToNew: (legacy) => ({
    id: legacy.legacy_id,
    name: legacy.legacy_name,
    ...legacy,
    migrated: true,
    migratedAt: new Date().toISOString()
  }),

  /**
   * Ajout de traçabilité et d’audit
   */
  addLegacyAuditTrail: (legacy) => {
    legacy.auditTrail = legacy.auditTrail || [];
    legacy.auditTrail.push({ date: new Date().toISOString(), action: 'audit' });
    return legacy;
  }
};
