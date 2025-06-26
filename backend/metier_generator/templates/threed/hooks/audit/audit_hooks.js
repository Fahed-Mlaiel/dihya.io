// Hooks audit threed (Node.js)
function beforeAudit(action, user) {
  // Logique avant audit
  return { action, user };
}
function afterAudit(action, user) {
  // Logique après audit
  return { action, user };
}
module.exports = { beforeAudit, afterAudit };
