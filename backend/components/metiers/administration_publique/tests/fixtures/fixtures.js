// fixtures.js – Fixtures avancés pour tests 3D, métiers et services
// Respecte la modularité, la réutilisabilité et la conformité RGPD

module.exports = {
  sample3DAsset: (overrides = {}) => ({
    id: 'asset-001',
    name: 'Asset Test',
    type: '3d',
    owner: 'user-001',
    createdAt: new Date().toISOString(),
    ...overrides
  }),
  sampleService: (overrides = {}) => ({
    id: 'service-001',
    name: 'Service Test',
    status: 'ok',
    environment: 'production',
    compliance: { rgpd: true, audit: true },
    ...overrides
  }),
  sampleUser: (overrides = {}) => ({
    id: 'user-001',
    username: 'testuser',
    roles: ['admin'],
    email: 'test@dihya.io',
    ...overrides
  })
};
