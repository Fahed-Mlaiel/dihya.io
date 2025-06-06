// index.js – Point d'entrée du module core pour l'API Threed (JS)
// Exporte le routeur Express et les services principaux

const api = require('./api');

module.exports = {
  ApiService: api,
  api
};
