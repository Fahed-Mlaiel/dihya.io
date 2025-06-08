// __init__.js – Initialisation avancée du dossier plugins (integration)
const fs = require('fs');
const path = require('path');
const plugins = {};
fs.readdirSync(__dirname).forEach(file => {
  if (file.startsWith('plugin_') && file.endsWith('.js')) {
    const mod = require(path.join(__dirname, file));
    plugins[file.replace('.js', '')] = mod;
  }
});
module.exports = plugins;
