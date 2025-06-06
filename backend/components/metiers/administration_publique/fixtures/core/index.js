// index.js - Point d'entrée principal pour fixtures/core (JS)
// Synchronisation JS/Python, conformité RGPD, accessibilité, audit, CI/CD, edge cases.
const models = require('./models');
const generators = require('../generators');
const samples = require('./samples');
module.exports = { ...models, ...generators, ...samples };
