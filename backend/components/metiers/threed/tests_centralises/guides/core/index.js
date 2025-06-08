// index.js – Exécution centralisée des tests guides/core (JS)
const { discoverAllTestsRecursively } = require('./__init__.js');
const path = require('path');
const allTests = discoverAllTestsRecursively(__dirname);
allTests.forEach(testPath => require(path.resolve(testPath)));
