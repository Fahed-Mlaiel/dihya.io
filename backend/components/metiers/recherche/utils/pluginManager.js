// pluginManager.js – Gestion dynamique des plugins pour Environnement (Node.js)
class PluginManager {
  constructor() {
    this.plugins = [];
  }
  register(plugin) {
    if (!this.plugins.includes(plugin)) {
      this.plugins.push(plugin);
    }
  }
  runAll(data) {
    return this.plugins.map(plugin => plugin.run(data));
  }
  getPlugins() {
    return this.plugins.map(p => p.constructor.name);
  }
}

module.exports = new PluginManager();
