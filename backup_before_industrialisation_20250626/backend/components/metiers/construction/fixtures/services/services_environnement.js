// services_environnement.js - Fixtures de services d'environnement pour Construction

module.exports = {
  getEnvInfo: () => ({
    env: process.env.NODE_ENV || 'test',
    status: 'ok',
    timestamp: new Date().toISOString(),
    features: ['construction', 'audit', 'plugins', 'multitenancy']
  }),
  mockEnv: {
    NODE_ENV: 'test',
    FEATURE_FLAG: true
  }
};
