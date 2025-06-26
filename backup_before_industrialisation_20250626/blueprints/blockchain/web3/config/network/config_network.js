// Gestion avancée de la configuration réseau blockchain (Node.js)
// Support multi-network, helpers, logs, validation
const logger = require('../../utils/logger').getLogger('config_network');

const NETWORKS = {
  mainnet: {
    chainId: 1,
    rpcUrl: 'https://mainnet.infura.io/v3/YOUR_PROJECT_ID'
  },
  goerli: {
    chainId: 5,
    rpcUrl: 'https://goerli.infura.io/v3/YOUR_PROJECT_ID'
  },
  sepolia: {
    chainId: 11155111,
    rpcUrl: 'https://sepolia.infura.io/v3/YOUR_PROJECT_ID'
  }
};

function getNetworkConfig(name) {
  const config = NETWORKS[name];
  if (!config) {
    logger.error(`Réseau inconnu: ${name}`);
    throw new Error(`Réseau inconnu: ${name}`);
  }
  logger.info(`Configuration réseau chargée: ${name}`);
  return config;
}

module.exports = { getNetworkConfig };
