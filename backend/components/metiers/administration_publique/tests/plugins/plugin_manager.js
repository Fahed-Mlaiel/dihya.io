// plugin_manager_js.js – Gestionnaire de plugins ultra avancé (clé en main, JS)
class PluginManager {
  constructor() {
    this.plugins = {};
  }
  register(name, plugin) {
    this.plugins[name] = plugin;
  }
  unregister(name) {
    delete this.plugins[name];
  }
  get(name) {
    return this.plugins[name];
  }
  listPlugins() {
    return Object.keys(this.plugins);
  }
  execute(name, ...args) {
    const plugin = this.get(name);
    if (plugin && typeof plugin.run === 'function') {
      return plugin.run(...args);
    }
    throw new Error(`Plugin '${name}' not found or invalid.`);
  }
}
module.exports = PluginManager;
