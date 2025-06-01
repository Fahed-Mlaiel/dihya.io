// Dihya Backend Assets – Plugin Loader (Node.js)
// Chargement dynamique de plugins backend, sécurité, audit, extensibilité

const fs = require('fs');
const path = require('path');

function loadPlugins(pluginsDir = './plugins') {
  const plugins = [];
  if (!fs.existsSync(pluginsDir)) return plugins;
  fs.readdirSync(pluginsDir).forEach(file => {
    if (file.endsWith('.js')) {
      const plugin = require(path.join(pluginsDir, file));
      if (plugin && plugin.enabled) {
        plugins.push(plugin);
        console.log(`[PLUGIN] Loaded: ${plugin.name}`);
      }
    }
  });
  return plugins;
}

module.exports = { loadPlugins };
// Usage: const { loadPlugins } = require('./plugin_loader');
// const plugins = loadPlugins();
