// index.js ultra avancé pour le domaine Plugins (Node.js)
// Point d'entrée centralisé pour tous les plugins métiers, audit, générateurs, etc.

const auditPlugin = require('./audit/audit_plugin');
// Ajoutez ici d'autres plugins ou générateurs à exposer

module.exports = {
  auditPlugin,
  // Ajoutez d'autres exports ici selon l'évolution du socle
};

/**
 * Exemple d'utilisation :
 * const { auditPlugin } = require('./plugins');
 * auditPlugin.runAudit();
 */
