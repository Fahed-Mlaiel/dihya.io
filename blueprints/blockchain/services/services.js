// Point d'entrée harmonisé pour tous les services blockchain
const ServicesIndex = require('./index');
const monitoringService = require('./monitoring-service');
const backupService = require('./backup-service');
const apiService = require('./apiService');
const oracleService = require('./oracle_service');
const interactContract = require('./interact_contract');
const webhookService = require('./webhookService');
const indexerService = require('./indexer_service');
const notificationService = require('./notification-service');
const schedulerService = require('./scheduler');
const InteractNFT = require('./interact_nft');

module.exports = {
  ServicesIndex,
  monitoringService,
  backupService,
  apiService,
  oracleService,
  interactContract,
  webhookService,
  indexerService,
  notificationService,
  schedulerService,
  InteractNFT
};
