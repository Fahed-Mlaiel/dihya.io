// __init__.js – Initialisation avancée du module de tests Plugins Threed (JS)
// Découverte automatique des tests, helpers, intégration CI/CD
const fs = require('fs');
const path = require('path');

function discoverTests() {
  return fs.readdirSync(__dirname).filter(f => f.endsWith('.test.js'));
}

function runAllTests() {
  discoverTests().forEach(test => require(path.join(__dirname, test)));
}

module.exports = { discoverTests, runAllTests };
