// services_environnement.js – Fixtures avancés de services d'environnement
// Respecte la conformité RGPD, la modularité et la logique métier
module.exports = [
  {
    id: 'service-001',
    name: 'Service Test',
    status: 'ok',
    environment: 'production',
    compliance: { rgpd: true, audit: true },
    lastChecked: new Date().toISOString()
  },
  {
    id: 'service-002',
    name: 'Service Secondaire',
    status: 'maintenance',
    environment: 'staging',
    compliance: { rgpd: false, audit: false },
    lastChecked: new Date().toISOString()
  }
];
