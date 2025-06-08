// __init__.js – Initialisation avancée du dossier mocks de fixtures de tests centralisés Threed
// Ce fichier permet l'import dynamique des mocks JS pour les tests, l'auto-discovery, et la compatibilité CI/CD.

const fs = require('fs');
const path = require('path');

const files = fs.readdirSync(__dirname);
files.forEach(file => {
  if (file.endsWith('.mock.js') && file !== 'index.js') {
    require(path.join(__dirname, file));
  }
});

// Point d'entrée pour l'extension de plugins de test, audit, RGPD, accessibilité, multi-langues, etc.
module.exports = {};
