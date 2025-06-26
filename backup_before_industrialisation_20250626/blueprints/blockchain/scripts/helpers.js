// helpers.js – Fonctions utilitaires pour scripts blockchain

/**
 * Valide la structure d’un asset
 * @param {Object} asset
 * @returns {boolean}
 */
function isValidAsset(asset) {
  return !!asset && typeof asset.id === 'string' && asset.id.length > 0;
}

/**
 * Génère un identifiant unique pour un asset
 * @returns {string}
 */
function generateAssetId() {
  return 'nft-' + Math.random().toString(36).substring(2, 10);
}

module.exports = { isValidAsset, generateAssetId };
