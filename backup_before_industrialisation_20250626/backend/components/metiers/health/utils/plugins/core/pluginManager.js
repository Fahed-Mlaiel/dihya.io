// pluginManager.js – Gestionnaire de plugins avancé pour Health (health)
// Fichier déplacé dans samples/pluginManager.js
class PluginManager {
  constructor() {
    this.plugins = [];
  }
  register(plugin) {
    this.plugins.push(plugin);
  }
  runAll(...args) {
    return this.plugins.map(plugin => plugin(...args));
  }
  list() {
    return this.plugins.map(p => p.name || 'anonymous');
  }
}

const pluginManager = new PluginManager();
module.exports = { pluginManager };
