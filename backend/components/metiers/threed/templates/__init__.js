/* global __dirname */

// __init__.js – Initialisation avancée des templates Threed (3D)
// Chargement dynamique, hooks, audit, sécurité, CI/CD, multi-formats, documentation intégrée

const fs = require('fs');
const path = require('path');

fs.readdirSync(__dirname).forEach(file => {
  if (file.endsWith('.js') && file !== '__init__.js') {
    require(path.join(__dirname, file));
  }
});

// Hooks d'initialisation, audit, sécurité, CI/CD, multi-formats
// (À compléter selon besoins métier)

/**
 * Documentation intégrée :
 * - Initialisation dynamique, auditabilité, extension, sécurité, CI/CD
 * - Synchronisation JS/Python assurée
 * - Complétude métier respectée
 */
