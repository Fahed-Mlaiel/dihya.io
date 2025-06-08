// __init__.js – Initialisation avancée du module de tests guides/helpers/services (JS)
const fs = require('fs');
const path = require('path');
function discoverTests() {
  return fs.readdirSync(__dirname).filter(f => f.endsWith('.test.js'));
}
function runAllTests() {
  discoverTests().forEach(test => require(path.join(__dirname, test)));
}
function discoverAllTestsRecursively(dir) {
  let results = [];
  fs.readdirSync(dir).forEach(file => {
    const filePath = path.join(dir, file);
    if (fs.statSync(filePath).isDirectory()) {
      results = results.concat(discoverAllTestsRecursively(filePath));
    } else if (file.endsWith('.test.js')) {
      results.push(filePath);
    }
  });
  return results;
}
module.exports = { discoverTests, runAllTests, discoverAllTestsRecursively };
