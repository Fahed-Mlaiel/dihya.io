// Initialisation avancée des blueprints DevOps (Node.js)
// Exports centralisés, auto-discovery, extension dynamique, documentation intégrée
const pipelines = require('./pipelines');
const scripts = require('./scripts');
const monitoring = require('./monitoring');
const { runFullDevOpsPipeline } = require('./pipelines/ci_cd');
module.exports = {
  pipelines,
  scripts,
  monitoring,
  runFullDevOpsPipeline
};
/**
 * Exemple d'utilisation :
 * const { runFullDevOpsPipeline } = require('./devops');
 * runFullDevOpsPipeline({ repo: '...', env: '...' });
 */
