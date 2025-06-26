// helper_audit.js – Helpers d’audit (JS)
function logAuditEvent(event) {
  if (typeof global.console.log === 'function') {
    global.console.log(`AUDIT: ${event}`);
  }
}
module.exports = { logAuditEvent };
