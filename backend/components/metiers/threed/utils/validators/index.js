// index.js – Point d'entrée JS pour les utilitaires validators du module threed
// Exporte toutes les fonctions principales et helpers (core, helpers, fallback)
const core = require('./core/validators');
const helpers = require('./helpers/validators_helper');
const fallback = require('./fallback/fallback');

function validateEmail(email) {
  return /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email);
}

module.exports = {
  ...core,
  ...helpers,
  ...fallback,
  isValidModel: core.isValidModel,
  validateRequired: core.validateRequired,
  validateEmail,
  validatorsHelper: helpers,
  fallbackValidate: fallback.validatorFallback
};
