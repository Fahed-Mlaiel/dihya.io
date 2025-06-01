// Module métier : __automatisation_de_tâches_métiers
// Orchestrateur de tâches métiers multi-stack (Node, Python, Bash, etc.)

const cron = require('node-cron');
const { exec } = require('child_process');

function planifierTache(cronExpr, commande) {
  return cron.schedule(cronExpr, () => {
    exec(commande, (err, stdout, stderr) => {
      if (err) {
        console.error('Erreur tâche automatisée:', err);
      } else {
        console.log('Tâche exécutée:', stdout);
      }
    });
  });
}

module.exports = { planifierTache };
