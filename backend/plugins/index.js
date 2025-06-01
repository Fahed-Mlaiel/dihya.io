// index.js – Dihya Backend Plugins

// Point d’entrée pour l’import/export des plugins backend
// Exemples d’utilisation, conventions, scripts d’automatisation

// Mock plugins métiers (chargement dynamique, hook)
function loadPlugin(name) { return { name, run: () => 'ok' }; }
function runPluginHook(plugin, action, data) { return { plugin: plugin.name, action, data, result: plugin.run() }; }
module.exports = { loadPlugin, runPluginHook };

// ...à compléter selon la stack backend choisie...
