// services_environnement.js - Fixtures de services d'environnement pour ServicesPersonne

module.exports = {
  getEnvInfo: () => ({
    env: process.env.NODE_ENV || 'test',
    status: 'ok',
    timestamp: new Date().toISOString(),
    features: ['services_personne', 'audit', 'plugins', 'multitenancy']
  }),
  mockEnv: {
    NODE_ENV: 'test',
    FEATURE_FLAG: true
  }
};
