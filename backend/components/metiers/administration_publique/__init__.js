// __init__.js
// Point d'entrée principal pour l'initialisation du module Threed
// Conforme au cahier des charges Dihya (2025)

const api = require('./api');
const services = require('./services');
const templates = require('./templates');
const views = require('./views');

module.exports = {
  api,
  services,
  templates,
  views,
  // Ajoutez ici d'autres exports nécessaires selon l'évolution métier
};
