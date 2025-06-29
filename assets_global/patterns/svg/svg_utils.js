// Fonctions utilitaires pour la gestion des assets SVG

function validateSvgAsset(asset) {
  // Validation basique
  return typeof asset === 'string' && asset.endsWith('.svg');
}

module.exports = { validateSvgAsset };
