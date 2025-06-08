// helpers_rbac.js
// Helpers avancés pour la gestion des rôles et permissions dynamiques

function assignRole(user, role) {
  // Simule l’assignation d’un rôle à un utilisateur
  return { ...user, roles: [...(user.roles || []), role] };
}

function checkPermission(user, permission) {
  // Simule la vérification d’une permission
  return user && user.permissions && user.permissions.includes(permission);
}

module.exports = { assignRole, checkPermission };
