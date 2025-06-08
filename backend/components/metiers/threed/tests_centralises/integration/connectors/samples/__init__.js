// __init__.js – Initialisation avancée des tests d'intégration Samples
const fs = require('fs');
const path = require('path');
const tests = {};
fs.readdirSync(__dirname).forEach(file => {
  if (file.startsWith('test_') && file.endsWith('.js')) {
    const mod = require(path.join(__dirname, file));
    tests[file.replace('.js', '')] = mod;
  }
});
module.exports = tests;
