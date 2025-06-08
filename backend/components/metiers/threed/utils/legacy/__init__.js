// Initialisation avancée du module legacy JS
const fs = require('fs');
const path = require('path');

function discoverLegacy(dir) {
  let results = [];
  fs.readdirSync(dir).forEach(file => {
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      results = results.concat(discoverLegacy(fullPath));
    } else if (file.endsWith('.js')) {
      results.push(fullPath);
    }
  });
  return results;
}

module.exports = {
  discoverLegacy,
};
