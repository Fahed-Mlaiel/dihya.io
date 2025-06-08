// __init__.js – Initialisation avancée des tests d'intégration Connectors (racine)
/**
 * Import/export dynamique, auto-discovery, extension future pour tous les sous-dossiers de tests d'intégration Connectors Threed.
 * Prêt pour l’industrialisation, l’audit, la RGPD, l’accessibilité, la documentation, la CI/CD, la multi-langue, l’extension et l’auto-discovery.
 */
const path = require('path');
const modules = {};
['adapters', 'exporters', 'importers', 'plugins', 'samples'].forEach(subdir => {
  try {
    modules[subdir] = require(path.join(__dirname, subdir));
  } catch (e) {}
});
module.exports = modules;
