// sample_usage.js
// Exemple d'utilisation du module RBAC (JS)
const rbac = require('../core/rbac_core');
const data = require('./sample_rbac_data.json');

// Vérification de permission
console.log('Peut lire ?', rbac.checkPermission(data.user, 'read'));

// Rôles de l'utilisateur
console.log('Rôles:', rbac.getUserRoles(data.user));
