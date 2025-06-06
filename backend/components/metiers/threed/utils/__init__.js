/* global __dirname */
/*
__init__.js – Initialisation avancée du dossier utils pour le module threed
- Import dynamique de tous les modules utilitaires
- Compatibilité CI/CD, audit, coverage
- Chargement automatique des helpers, plugins, validators, exporters, etc.
- Documentation intégrée pour audit et conformité
*/
const fs = require('fs');
const path = require('path');

fs.readdirSync(__dirname)
  .filter(f => f.endsWith('.js') && f !== '__init__.js')
  .forEach(f => require(path.join(__dirname, f)));

// __init__.js – Initialisation avancée JS pour CI/CD, audit, conformité
module.exports = require('./index');
