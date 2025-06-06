// services_environnement.js – Ultra-robuste Services-Liste für Environnement (Dihya Coding)
module.exports = [
  {
    id: 1,
    service: 'Audit environnemental',
    description: "Service d'audit pour la conformité environnementale (RGPD, audit, multilingue, plugins, CI/CD).",
    type: 'audit',
    statut: 'actif',
    date_creation: '2025-06-02T00:00:00Z',
    date_modification: '2025-06-02T00:00:00Z',
    audit: {
      created_by: 'test_admin',
      created_at: '2025-06-02T00:00:00Z',
      rgpd: true,
      plugins: ['sample_plugin'],
      i18n: ['fr', 'en', 'ar']
    }
  },
  {
    id: 2,
    service: 'Export RGPD',
    description: 'Export automatisé des données environnementales (RGPD, audit, CI/CD).',
    type: 'export',
    statut: 'actif',
    date_creation: '2025-06-02T00:00:00Z',
    date_modification: '2025-06-02T00:00:00Z',
    audit: {
      created_by: 'test_admin',
      created_at: '2025-06-02T00:00:00Z',
      rgpd: true,
      plugins: ['exporter_plugin'],
      i18n: ['fr', 'en']
    }
  }
];
