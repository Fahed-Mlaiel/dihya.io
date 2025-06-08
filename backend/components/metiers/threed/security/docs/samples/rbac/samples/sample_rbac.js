// sample_rbac.js
// Exemple d’intégration avancée pour la gestion des rôles

const { assignRole, checkPermission } = require('./helpers_rbac');

let user = { id: 'u123', name: 'Alice', permissions: ['read'] };
user = assignRole(user, 'admin');
console.log('Roles:', user.roles);
console.log('Has read:', checkPermission(user, 'read'));
console.log('Has write:', checkPermission(user, 'write'));
