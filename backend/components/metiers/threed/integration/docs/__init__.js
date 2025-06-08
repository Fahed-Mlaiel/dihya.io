// __init__.js – Initialisation avancée du dossier docs (integration)
const fs = require('fs');
const path = require('path');
const docs = {};
fs.readdirSync(__dirname).forEach(file => {
  if (file.startsWith('doc_') && file.endsWith('.js')) {
    const mod = require(path.join(__dirname, file));
    docs[file.replace('.js', '')] = mod;
  }
});
module.exports = docs;
