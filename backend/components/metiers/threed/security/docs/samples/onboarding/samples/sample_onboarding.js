// sample_onboarding.js
// Exemple d’intégration avancée pour l’onboarding

const { startOnboarding, completeOnboarding } = require('./helpers_onboarding');

let user = { id: 'u123', name: 'Alice' };
user = startOnboarding(user);
console.log('Started:', user);
user = completeOnboarding(user);
console.log('Completed:', user);
