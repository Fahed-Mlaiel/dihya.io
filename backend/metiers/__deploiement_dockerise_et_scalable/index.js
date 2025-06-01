// Module métier : __déploiement_dockerisé_et_scalable
// Fournit l’infrastructure et les scripts pour un déploiement dockerisé/scalable multi-stack.

const { exec } = require('child_process');

function deploiementDockerCompose() {
  exec('docker-compose up -d', (err, stdout, stderr) => {
    if (err) {
      console.error('Erreur déploiement Docker:', err);
    } else {
      console.log('Déploiement Docker réussi:', stdout);
    }
  });
}

module.exports = { deploiementDockerCompose };
