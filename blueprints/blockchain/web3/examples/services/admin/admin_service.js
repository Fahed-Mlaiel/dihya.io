// Service avancé pour administration de smart contract (pause, transfert propriété, logs, helpers, gestion d'erreurs)
const { sendTransaction } = require('../contract/contract_service');
const logger = require('../../utils/logger').getLogger('admin_service');

async function pauseContract() {
  try {
    const receipt = await sendTransaction('pause');
    logger.info(`Contrat mis en pause: ${JSON.stringify(receipt)}`);
    return receipt;
  } catch (e) {
    logger.error(`Erreur pause: ${e}`);
    return null;
  }
}

async function transferOwnership(newOwner) {
  try {
    const receipt = await sendTransaction('transferOwnership', newOwner);
    logger.info(`Transfert propriété à ${newOwner}: ${JSON.stringify(receipt)}`);
    return receipt;
  } catch (e) {
    logger.error(`Erreur transfert propriété ${newOwner}: ${e}`);
    return null;
  }
}

module.exports = { pauseContract, transferOwnership };

module.exports = { admin_service };
