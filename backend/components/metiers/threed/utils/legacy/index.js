// Index centralisé pour l’export de tous les modules legacy JS
const { discoverLegacy } = require('./__init__.js');
const path = require('path');

const legacyFiles = discoverLegacy(__dirname);

legacyFiles.forEach(legacyFile => {
  require(legacyFile);
});

module.exports = legacyFiles;
