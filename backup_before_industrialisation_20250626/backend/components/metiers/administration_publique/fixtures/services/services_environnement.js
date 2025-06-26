// services_environnement.js - Fixtures de services d'environnement pour administration_publique

module.exports = {
  getEnvInfo: () => ({
    env: process.env.NODE_ENV || 'test',
    status: 'ok',
    timestamp: new Date().toISOString(),
    features: ['administration_publique', 'audit', 'plugins', 'multitenancy']
  }),
  mockEnv: {
    NODE_ENV: 'test',
    FEATURE_FLAG: true
  }
};
