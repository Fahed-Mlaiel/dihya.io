// __init__.js – Initialisation avancée du sous-module core (tests API)
const fs = require('fs');
const path = require('path');
function discoverTests() {
  return fs.readdirSync(__dirname).filter(f => f.endsWith('.test.js'));
}
function runAllTests() {
  discoverTests().forEach(test => require(path.join(__dirname, test)));
}
module.exports = { discoverTests, runAllTests };
