// Exemple avancé gestion des permissions (Node.js)
function grantPermission(role, resource, action) {
  // Logique d’attribution de permission
  return `Permission ${action} sur ${resource} accordée à ${role}.`;
}

module.exports = { grantPermission };
