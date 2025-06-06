// guides/helpers/helpers_plugins.js – Helpers avancés pour guides plugins

function validatePluginConfig(config) {
  // Validation avancée de la config plugin
  if (!config || typeof config !== 'object') throw new Error('Config plugin invalide');
  if (!config.name || !config.version) throw new Error('Nom et version requis');
  return true;
}

// helpers_plugins.js – Helpers ultra avancés plugins (JS)
module.exports = {
  checkPlugin: (data) => {
    return !!data.enabled && !!data.version;
  },
  auditPlugin: (data) => {
    let score = 0;
    if (data.enabled) score += 50;
    if (data.version) score += 50;
    return { score, compliant: score === 100 };
  }
};

module.exports = { validatePluginConfig };
