/**
 * Plugin Manager VR/AR – Dihya Coding
 * Système de plugins extensible pour VR/AR (ajout, suppression, exécution, audit, sécurité, RGPD)
 * @module plugins/vr_ar
 * @author Dihya Team
 * @since 2025-05-25
 */
const availablePlugins = {
  'emotion_analysis': require('./plugins/vr_ar/emotion_analysis'),
  // Ajoutez d'autres plugins ici
};

function pluginManager(moduleName) {
  return (req, res, next) => {
    const pluginName = req.query.plugin;
    if (!pluginName || !availablePlugins[pluginName]) {
      return res.status(400).json({ success: false, error: req.t('error.plugin_not_found') });
    }
    try {
      const result = availablePlugins[pluginName].run(req);
      res.status(200).json({ success: true, result });
    } catch (err) {
      res.status(500).json({ success: false, error: req.t('error.plugin_failed') });
    }
  };
}

module.exports = { pluginManager };
