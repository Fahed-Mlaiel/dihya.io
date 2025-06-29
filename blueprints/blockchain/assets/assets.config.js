// assets.config.js – Configuration centralisée et helpers métiers pour les assets blockchain

const i18n = require('./i18n.assets.json');

const assetConfig = {
  theme: {
    primaryColor: '#0055B7',
    secondaryColor: '#007A3D',
    font: 'Open Sans, Arial, sans-serif'
  },
  i18n,
  accessibility: {
    defaultAlt: {
      fr: 'Image par défaut',
      en: 'Default image',
      ar: 'الصورة الافتراضية'
    }
  }
};

/**
 * Récupère la config d’un asset par langue
 * @param {string} lang
 * @returns {Object}
 */
function getAssetConfig(lang = 'fr') {
  return {
    ...assetConfig,
    i18n: assetConfig.i18n[lang] || assetConfig.i18n['fr']
  };
}

/**
 * Valide la structure d’un asset
 * @param {Object} asset
 * @returns {boolean}
 */
function validateAsset(asset) {
  return !!asset && typeof asset.id === 'string' && asset.id.length > 0;
}

module.exports = {
  assetConfig,
  getAssetConfig,
  validateAsset
};
