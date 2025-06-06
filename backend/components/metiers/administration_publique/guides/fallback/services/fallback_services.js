// guides/fallback/fallback_services.js – Fallbacks et tests avancés pour guides services

function fallbackServiceConfig() {
  // Fallback de configuration service pour tests d’intégration
  return {
    name: 'service-fallback',
    endpoint: '/api/fallback',
    description: 'Fallback de test pour service',
  };
}

module.exports = { fallbackServiceConfig };
