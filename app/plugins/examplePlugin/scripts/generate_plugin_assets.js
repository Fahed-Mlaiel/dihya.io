// Script d’automatisation pour générer ou mettre à jour les assets du plugin

const fs = require('fs');

function generateAssets() {
  // Exemple : création d’un fichier asset fictif
  fs.writeFileSync('assets/generated_asset.txt', 'Asset généré automatiquement.');
  console.log('Asset généré.');
}

generateAssets();
