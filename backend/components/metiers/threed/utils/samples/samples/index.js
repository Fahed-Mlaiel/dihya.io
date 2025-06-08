// index.js – Exécution centralisée des samples/samples JS
const path = require('path');
const fs = require('fs');
function discoverSamples(dir) {
  let results = [];
  fs.readdirSync(dir).forEach(file => {
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      results = results.concat(discoverSamples(fullPath));
    } else if (file.endsWith('.js') && !file.startsWith('index') && !file.startsWith('__init__')) {
      results.push(fullPath);
    }
  });
  return results;
}
const samplesRoot = __dirname;
const allSamples = discoverSamples(samplesRoot);
allSamples.forEach(sample => {
  require(sample);
});
module.exports = { allSamples };
