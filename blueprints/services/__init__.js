// Initialisation avancée des services métier (Node.js)
// Découverte et export automatique des services du dossier

const { AssetService } = require('./asset_service');

/**
 * Exporte tous les services métier du dossier
 * @module services
 */
module.exports = {
  AssetService
};

/**
 * Exemple d'utilisation :
 * const { AssetService } = require('./services');
 * const service = new AssetService();
 * const asset = service.create({ name: 'Ordinateur' });
 * console.log(asset);
 */
