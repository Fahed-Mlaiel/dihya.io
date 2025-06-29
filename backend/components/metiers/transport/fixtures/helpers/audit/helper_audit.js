/* global console */
const console = require('console');
// helper_audit.js – Helpers d’audit (JS)
function logAuditEvent(event) {
  console.log(`AUDIT: ${event}`);
}
module.exports = { logAuditEvent };
