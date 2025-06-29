// index.js ultra avancé pour le domaine DevOps (Node.js)
// Point d'entrée centralisé pour pipelines, scripts, monitoring, CI/CD, etc.

const ciCd = require('./pipelines/ci_cd');
const monitoring = require('./monitoring/monitoring');
const devopsScripts = require('./scripts/devops');
// Ajoutez ici d'autres modules DevOps à exposer

module.exports = {
  ciCd,
  monitoring,
  devopsScripts,
  // Ajoutez d'autres exports ici selon l'évolution du socle
};

/**
 * Exemple d'utilisation :
 * const { ciCd, monitoring } = require('./devops');
 * ciCd.runPipeline();
 * monitoring.sendAlert('Incident détecté');
 */
