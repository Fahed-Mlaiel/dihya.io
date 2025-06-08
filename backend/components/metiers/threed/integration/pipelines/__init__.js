// __init__.js – Initialisation avancée du dossier pipelines (integration)
const fs = require('fs');
const path = require('path');
const pipelines = {};
fs.readdirSync(__dirname).forEach(file => {
  if (file.startsWith('pipeline_') && file.endsWith('.js')) {
    const mod = require(path.join(__dirname, file));
    pipelines[file.replace('.js', '')] = mod;
  }
});
module.exports = pipelines;
