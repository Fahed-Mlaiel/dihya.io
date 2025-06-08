// sample_route.js - Exemple métier avancé route imbriquée
function sampleRoute(user, action) {
  if (!user || !user.role) return false;
  if (user.role === 'admin') return true;
  if (user.role === 'user' && action === 'read') return true;
  return false;
}
module.exports = sampleRoute;
