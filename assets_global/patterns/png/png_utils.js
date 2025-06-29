// Fonctions utilitaires pour la gestion des assets PNG

function validatePngAsset(asset) {
  // Validation basique
  return typeof asset === 'string' && asset.endsWith('.png');
}

module.exports = { validatePngAsset };
