// __init__.js – Initialisation avancée du module de tests centralisés threed (JS)
// Découverte automatique, helpers, CI/CD, documentation clé en main
const fs = require('fs');
const path = require('path');

/**
 * Découverte automatique de tous les fichiers de tests JS dans tous les sous-modules.
 * @returns {string[]} Liste des chemins de fichiers .test.js
 */
module.exports.discover = () => {
  const walk = dir => fs.readdirSync(dir).flatMap(f => {
    const p = path.join(dir, f);
    return fs.statSync(p).isDirectory() ? walk(p) : p;
  });
  return walk(__dirname).filter(f => f.endsWith('.test.js'));
};
