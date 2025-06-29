// templates_mock.js – Mocks pour tests unitaires et intégration des templates Juridique (JS)
// Inclut : scénarios spécifiques, edge cases, CI/CD, audit, accessibilité

module.exports = {
  mockRapportAudit: { date: '2025-06-03', result: 'OK' },
  mockEmailNotification: { details: 'Nouvelle scène juridique créée' },
  mockAccessibiliteAudit: { date: '2025-06-03' },
  mockServiceExport: { date: '2025-06-03' }
};
// Utilisable pour tests e2e, migration massive, CI/CD
