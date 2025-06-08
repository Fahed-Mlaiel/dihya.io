// sample_advanced.js - Exemple métier avancé RBAC
function advancedSampleRBAC(user, action) {
  if (!user || !user.role) return false;
  if (user.role === 'admin') return true;
  if (user.role === 'user' && action === 'read') return true;
  return false;
}
module.exports = advancedSampleRBAC;
