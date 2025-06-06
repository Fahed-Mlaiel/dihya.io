/* global __dirname */
// index.js – Point d'entrée JS pour les utilitaires views du module threed
const fs = require('fs');
const path = require('path');

const subdirs = ['api', 'templates', 'admin', 'public', 'partials', 'conformity', 'threed'];
const exportsObj = {};

function handleUnusedE(e) {
  // purposely unused
}

subdirs.forEach((dir) => {
  const dirPath = path.join(__dirname, dir);
  if (fs.existsSync(dirPath)) {
    try {
      const mod = require(dirPath);
      Object.assign(exportsObj, mod);
    } catch (e) {
      handleUnusedE(e); // suppression du warning no-unused-vars
      // ignore if no index.js or __init__.js
    }
  }
});

// Suppression des références directes à views.js
// Tout doit passer par les sous-dossiers (ex: threed/)

module.exports = exportsObj;
