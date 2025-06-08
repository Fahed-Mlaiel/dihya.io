// __init__.js – Initialisation avancée du dossier integration (racine)
/**
 * Import/export dynamique, auto-discovery, extension future pour tous les sous-dossiers d'intégration Threed.
 * Prêt pour l’industrialisation, l’audit, la RGPD, l’accessibilité, la documentation, la CI/CD, la multi-langue, l’extension et l’auto-discovery.
 */
const path = require('path');
const modules = {};
['connectors', 'docs', 'pipelines', 'plugins', 'samples', 'scripts'].forEach(subdir => {
  try {
    modules[subdir] = require(path.join(__dirname, subdir));
  } catch (e) {}
});
module.exports = modules;
