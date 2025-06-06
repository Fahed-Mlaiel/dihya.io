// Exemple de helper d’audit (JS)
function sampleAuditLog(userId, action) {
  console.log(`[AUDIT] Utilisateur: ${userId}, Action: ${action}`);
  return true;
}
module.exports = { sampleAuditLog };
