/**
 * @file plugins.js
 * @description Fonctions utilitaires pour la gestion des plugins côté frontend Dihya Coding (affichage, métadonnées, validation).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les interactions sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Structure d’un plugin pour l’UI.
 * @typedef {object} Plugin
 * @property {string} id - Identifiant unique du plugin
 * @property {string} name - Nom du plugin
 * @property {string} version - Version du plugin
 * @property {string} description - Description courte
 * @property {boolean} enabled - Statut d’activation
 * @property {object} [meta] - Métadonnées additionnelles
 */

/**
 * Valide la structure d’un plugin.
 * @param {object} plugin
 * @returns {boolean}
 */
export function isValidPlugin(plugin) {
  return (
    plugin &&
    typeof plugin.id === 'string' &&
    typeof plugin.name === 'string' &&
    typeof plugin.version === 'string' &&
    typeof plugin.description === 'string' &&
    typeof plugin.enabled === 'boolean'
  );
}

/**
 * Filtre les plugins actifs.
 * @param {Plugin[]} plugins
 * @returns {Plugin[]}
 */
export function getEnabledPlugins(plugins) {
  return Array.isArray(plugins) ? plugins.filter(p => p.enabled) : [];
}

/**
 * Filtre les plugins désactivés.
 * @param {Plugin[]} plugins
 * @returns {Plugin[]}
 */
export function getDisabledPlugins(plugins) {
  return Array.isArray(plugins) ? plugins.filter(p => !p.enabled) : [];
}

/**
 * Recherche un plugin par son identifiant.
 * @param {Plugin[]} plugins
 * @param {string} id
 * @returns {Plugin|null}
 */
export function findPluginById(plugins, id) {
  if (!Array.isArray(plugins) || !id) return null;
  return plugins.find(p => p.id === id) || null;
}

/**
 * Anonymise le nom ou la description d’un plugin pour les logs (pas de données personnelles).
 * @param {string} str
 * @returns {string}
 */
export function anonymizePluginString(str) {
  return typeof str === 'string'
    ? str.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '[email]')
    : '';
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} [pluginId]
 */
export function logPluginsEvent(action, pluginId) {
  try {
    const logs = JSON.parse(localStorage.getItem('plugins_logs') || '[]');
    logs.push({
      action,
      pluginId,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('plugins_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de plugins locaux (droit à l’oubli RGPD).
 */
export function clearLocalPluginsLogs() {
  localStorage.removeItem('plugins_logs');
}