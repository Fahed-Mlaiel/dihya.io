// Initialisation avancée du module JS
const fs = require('fs');
const path = require('path');

function discoverTests(dir) {
  let results = [];
  fs.readdirSync(dir).forEach(file => {
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      results = results.concat(discoverTests(fullPath));
    } else if (file.endsWith('.test.js')) {
      results.push(fullPath);
    }
  });
  return results;
}

module.exports = {
  discoverTests,
};
