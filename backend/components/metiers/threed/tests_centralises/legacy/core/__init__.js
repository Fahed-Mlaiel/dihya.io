// Initialisation du module de tests legacy/core
// Découverte automatique, helpers, CI/CD
const fs = require('fs');
module.exports.discover = () => {
  return fs.readdirSync(__dirname).filter(f => f.endsWith('.test.js'));
};

function discoverAllTestsRecursively(dir) {
  const fs = require('fs');
  const path = require('path');
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

module.exports = { ...module.exports, discoverAllTestsRecursively };
