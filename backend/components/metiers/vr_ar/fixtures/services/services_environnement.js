// services_environnement.js - Fixtures de services d'environnement pour vr_ar

module.exports = {
  getEnvInfo: () => ({
    env: process.env.NODE_ENV || 'test',
    status: 'ok',
    timestamp: new Date().toISOString(),
    features: ['vr_ar', 'audit', 'plugins', 'multitenancy']
  }),
  mockEnv: {
    NODE_ENV: 'test',
    FEATURE_FLAG: true
  }
};
