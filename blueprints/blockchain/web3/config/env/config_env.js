// Gestion avancée de la configuration d'environnement (Node.js)
// Chargement dynamique, validation, logs, helpers
require('dotenv').config();
const logger = require('../../utils/logger').getLogger('config_env');

const REQUIRED_VARS = [
  'INFURA_URL', 'PRIVATE_KEY', 'ACCOUNT_ADDRESS', 'CONTRACT_ADDRESS'
];

function getEnvVar(key, def = undefined) {
  const value = process.env[key] || def;
  if (value === undefined) {
    logger.error(`Variable d'environnement manquante: ${key}`);
    throw new Error(`Variable d'environnement manquante: ${key}`);
  }
  return value;
}

function validateEnv() {
  REQUIRED_VARS.forEach(getEnvVar);
  logger.info('Toutes les variables d\'environnement requises sont présentes.');
}

validateEnv();

module.exports = { getEnvVar, validateEnv };

module.exports = { config_env };
