// index.js - Point d'entrée principal pour accessibility (JS)
const guides = require('./guides');
const samples = require('./samples');
module.exports = { ...guides, ...samples };
