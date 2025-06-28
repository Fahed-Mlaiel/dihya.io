// plugins_helper.js
// Ultra-avancé, clé en main : helpers pour la gestion des plugins selon le cahier des charges et la logique métier

/**
 * Enregistre un plugin dans le système.
 * @param {object} registry - Le registre global des plugins.
 * @param {object} plugin - Le plugin à enregistrer (doit avoir id, name, et init).
 * @returns {boolean}
 */
function registerPlugin(registry, plugin) {
  if (!plugin || typeof plugin.id !== 'string' || typeof plugin.name !== 'string' || typeof plugin.init !== 'function') {
    return false;
  }
  if (registry[plugin.id]) {
    return false; // déjà enregistré
  }
  registry[plugin.id] = plugin;
  return true;
}

/**
 * Initialise tous les plugins enregistrés.
 * @param {object} registry - Le registre global des plugins.
 * @param {object} context - Le contexte métier à passer à chaque plugin.
 */
function initAllPlugins(registry, context) {
  Object.values(registry).forEach(plugin => {
    if (typeof plugin.init === 'function') {
      plugin.init(context);
    }
  });
}

/**
 * Vérifie la conformité d’un plugin selon le cahier des charges.
 * @param {object} plugin
 * @returns {boolean}
 */
function isPluginCompliant(plugin) {
  return plugin && typeof plugin.id === 'string' && typeof plugin.name === 'string' && typeof plugin.init === 'function';
}

/**
 * Liste tous les plugins actifs.
 * @param {object} registry
 * @returns {object[]}
 */
function listActivePlugins(registry) {
  return Object.values(registry).filter(p => p.active !== false);
}

module.exports = {
  registerPlugin,
  initAllPlugins,
  isPluginCompliant,
  listActivePlugins,
};
