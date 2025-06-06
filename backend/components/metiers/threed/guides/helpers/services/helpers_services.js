// guides/helpers/helpers_services.js – Helpers avancés pour guides services

function validateServiceConfig(config) {
  // Validation avancée de la config service
  if (!config || typeof config !== 'object') throw new Error('Config service invalide');
  if (!config.name || !config.endpoint) throw new Error('Nom et endpoint requis');
  return true;
}

// helpers_services.js – Helpers ultra avancés services (JS)
module.exports = {
  checkService: (data) => {
    return data.status === 'ok' && data.uptime > 90;
  },
  auditService: (data) => {
    let score = 0;
    if (data.status === 'ok') score += 50;
    if (data.uptime > 90) score += 50;
    return { score, compliant: score === 100 };
  }
};

module.exports = { validateServiceConfig };
