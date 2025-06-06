// Restauration automatique du dossier industrie à partir du modèle environnement
const fs = require('fs');
const path = require('path');

const METIERS_ROOT = path.resolve(__dirname, 'backend/components/metiers');
const ENV_MODEL = path.join(METIERS_ROOT, 'environnement');
const DEST = path.join(METIERS_ROOT, 'industrie');

function copyRecursive(src, dest) {
  if (!fs.existsSync(dest)) fs.mkdirSync(dest);
  for (const file of fs.readdirSync(src)) {
    const srcPath = path.join(src, file);
    const destPath = path.join(dest, file);
    const stat = fs.statSync(srcPath);
    if (stat.isDirectory()) {
      copyRecursive(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

copyRecursive(ENV_MODEL, DEST);
console.log('Restauration du dossier industrie terminée.');
