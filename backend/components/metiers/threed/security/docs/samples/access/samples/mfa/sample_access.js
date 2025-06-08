// sample_access.js
// Exemple d’intégration avancée pour la gestion des accès

const { generateMfaToken, provisionUser } = require('../helpers');

// Provisionnement d’un utilisateur
const user = { id: 'u123', name: 'Alice' };
const provisioned = provisionUser(user);
console.log('Provisioned:', provisioned);

// Génération d’un token MFA
const mfaToken = generateMfaToken(user.id);
console.log('MFA Token:', mfaToken);
