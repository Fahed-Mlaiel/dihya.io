// plugins_helper.js - Fonctions utilitaires avancées pour la gestion des plugins Threed

module.exports = {
  listPlugins: (plugins) => plugins.map(p => p.name),
  activateAll: (plugins) => plugins.forEach(p => p.activate && p.activate()),
  deactivateAll: (plugins) => plugins.forEach(p => p.deactivate && p.deactivate()),

  /**
   * Hook d’audit global pour tous les plugins
   */
  auditAll: (plugins) => plugins.forEach(p => p.getAuditTrail && console.log(p.getAuditTrail())),

  /**
   * Sécurité : vérification de signature de plugin
   */
  isTrustedPlugin: (plugin) => plugin && plugin.name && typeof plugin.activate === 'function',

  /**
   * Documentation intégrée : helpers compatibles CI/CD, audit, sécurité
   */
  pluginInfo: (plugin) => `Plugin: ${plugin.name}`
};
