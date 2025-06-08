// index.js – Exécution centralisée des tests legacy (JS)
const { discoverAllTestsRecursively } = require('./__init__.js');
const path = require('path');
const allTests = discoverAllTestsRecursively(__dirname);
allTests.forEach(testPath => require(path.resolve(testPath)));
