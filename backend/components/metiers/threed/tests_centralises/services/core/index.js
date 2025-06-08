// index.js – Exécution centralisée des tests JS pour services/core
const requireDirectory = require('require-directory');
const path = require('path');

describe('Services Core – Centralised', () => {
  const modules = requireDirectory(module, __dirname, { visit: mod => mod });
  // Découverte récursive de tous les tests JS dans les sous-dossiers
  for (const key in modules) {
    if (modules[key] && typeof modules[key] === 'object') {
      // Les sous-modules sont automatiquement découverts
    }
  }
  // Les tests de chaque sous-module sont exécutés via require-directory
});
