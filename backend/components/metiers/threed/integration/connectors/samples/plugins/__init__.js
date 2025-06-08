// __init__.js – Initialisation avancée des exemples de plugins
const fs = require('fs');
const path = require('path');
const samples = {};
fs.readdirSync(__dirname).forEach(file => {
  if (file.startsWith('example_') && file.endsWith('.js')) {
    const mod = require(path.join(__dirname, file));
    samples[file.replace('.js', '')] = mod;
  }
});
module.exports = samples;
