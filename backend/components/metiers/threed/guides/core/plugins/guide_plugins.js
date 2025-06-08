// guide_plugins.js - Guide d'intégration et d'utilisation des plugins Threed (JS)

/**
 * Ce fichier explique comment intégrer, activer et tester des plugins JS dans le module Threed.
 *
 * Exemples :
 *   - Ajout dynamique d'un plugin
 *   - Activation/désactivation
 *   - Bonnes pratiques de sécurité et d'audit
 */

module.exports = {
  addPlugin: (manager, plugin) => manager.register(plugin),
  activatePlugin: (plugin) => plugin.activate && plugin.activate(),
  deactivatePlugin: (plugin) => plugin.deactivate && plugin.deactivate()
};

/**
 * Exemples avancés d'intégration de plugins :
 *
 * // Ajout dynamique
 * const plugin = { name: 'MyPlugin', activate: () => {}, deactivate: () => {} };
 * addPlugin(manager, plugin);
 *
 * // Sécurité : vérifier la signature du plugin
 * function isTrusted(plugin) { return plugin && plugin.name && plugin.activate; }
 *
 * // Audit : journaliser l'activation
 * function auditActivation(plugin) {
 *   console.log(`[AUDIT] Activation du plugin: ${plugin.name}`);
 * }
 *
 * // CI/CD : tests automatisés sur les plugins
 * // (voir tests/plugins.test.js)
 */
