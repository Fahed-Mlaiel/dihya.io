// Validation avancée d'asset
module.exports = function validateAsset(asset) {
  if (!asset.name) throw new Error('Le nom est requis');
  // Ajoutez d'autres règles métier ici
  return true;
};
