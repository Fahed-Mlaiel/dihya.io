// Initialisation du module de tests views
// Découverte automatique, helpers, CI/CD
const fs = require('fs');
const path = require('path');

function discoverTests() {
  return fs.readdirSync(__dirname).filter(f => f.endsWith('.test.js'));
}

function runAllTests() {
  discoverTests().forEach(test => require(path.join(__dirname, test)));
}

module.exports = { discoverTests, runAllTests };
