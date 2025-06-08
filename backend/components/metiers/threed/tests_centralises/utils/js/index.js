// Index centralisé pour l’exécution de tous les tests JS du module
const { discoverTests } = require('./__init__.js');
const path = require('path');

const testFiles = discoverTests(__dirname);

testFiles.forEach(testFile => {
  require(testFile);
});

console.log(`Tous les tests JS (${testFiles.length}) exécutés dans ${__dirname}`);
