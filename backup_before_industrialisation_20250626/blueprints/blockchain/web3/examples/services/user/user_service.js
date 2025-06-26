// Service avancé pour gestion d'utilisateurs blockchain (whitelist, solde, logs, helpers, gestion d'erreurs)
const { callMethod, sendTransaction } = require('../contract/contract_service');
const logger = require('../../utils/logger').getLogger('user_service');

async function addToWhitelist(address) {
  try {
    const receipt = await sendTransaction('addToWhitelist', address);
    logger.info(`Ajout ${address} à la whitelist: ${JSON.stringify(receipt)}`);
    return receipt;
  } catch (e) {
    logger.error(`Erreur ajout whitelist ${address}: ${e}`);
    return null;
  }
}

async function getBalance(address) {
  try {
    const balance = await callMethod('balanceOf', address);
    logger.info(`Solde de ${address} récupéré: ${balance}`);
    return balance;
  } catch (e) {
    logger.error(`Erreur solde ${address}: ${e}`);
    return null;
  }
}

module.exports = { addToWhitelist, getBalance };

module.exports = { user_service };
