// __init__.js – Initialisation avancée du module Threed (JS)
// Découverte automatique, helpers, CI/CD, documentation clé en main

const api = require('./api');
const services = require('./services');
const templates = require('./templates');
const views = require('./views');

/**
 * Découverte automatique des modules JS du sous-dossier threed.
 * @returns {object} Modules centralisés
 */
module.exports = {
  api,
  services,
  templates,
  views,
  // Ajoutez ici d'autres exports nécessaires selon l'évolution métier
};
