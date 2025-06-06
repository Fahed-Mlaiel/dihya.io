// index.js - Point d'entrée principal pour mocks (JS)
const core = require('./core');
const samples = require('./samples');
module.exports = { ...core, ...samples };
