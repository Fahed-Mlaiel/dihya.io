// PluginManager pour la gestion des plugins blockchain
class PluginManager {
  constructor() {
    this.plugins = [];
  }
  register(plugin) {
    this.plugins.push(plugin);
  }
  list() {
    return this.plugins;
  }
}
module.exports = PluginManager;

module.exports = { PluginManager };
