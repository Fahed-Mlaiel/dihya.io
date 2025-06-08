// sample_rgpd.js
// Exemple d’intégration avancée pour la conformité RGPD

const { anonymizeData, checkConsent } = require('./helpers_rgpd');

const user = { id: 'u123', name: 'Alice', consent: true };
console.log('Consent:', checkConsent(user));
console.log('Anonymized:', anonymizeData(user));
