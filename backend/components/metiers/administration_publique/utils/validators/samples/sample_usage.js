// sample_usage.js
// Exemple d'utilisation du module validators (JS)
const validators = require('../core/validators');
const data = require('./sample_validators_data.json');

// Validation d'email
console.log('Email valide ?', validators.validateEmail(data.email));

// Validation d'un champ obligatoire
console.log('Champ obligatoire valide ?', validators.validateRequired(data.requiredField));
