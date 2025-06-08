// __init__.js – Initialisation avancée du dossier scripts (integration)
const fs = require('fs');
const path = require('path');
const scripts = {};
fs.readdirSync(__dirname).forEach(file => {
  if (file.startsWith('script_') && file.endsWith('.js')) {
    const mod = require(path.join(__dirname, file));
    scripts[file.replace('.js', '')] = mod;
  }
});
module.exports = scripts;
