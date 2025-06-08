// Index centralisé pour l’exécution de tous les tests logger JS du module
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

const testFiles = discoverTests(__dirname);
testFiles.forEach(testFile => {
  require(testFile);
});
console.log(`Tous les tests logger JS (${testFiles.length}) exécutés dans ${__dirname}`);
