const fs = require('fs');
const path = require('path');
function discoverSamples(dir) {
  let results = [];
  fs.readdirSync(dir).forEach(file => {
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      results = results.concat(discoverSamples(fullPath));
    } else if (file.endsWith('.js') && !file.startsWith('__init__')) {
      results.push(fullPath);
    }
  });
  return results;
}
module.exports = { discoverSamples };
