// sample_compliance.js
// Exemple d’intégration avancée pour la conformité

const { checkCompliance, generateComplianceReport } = require('./helpers_compliance');

const data = { entity: 'ACME Corp', standards: ['ISO27001', 'SOC2'] };
console.log('ISO27001:', checkCompliance('ISO27001', data));
console.log(generateComplianceReport(data));
