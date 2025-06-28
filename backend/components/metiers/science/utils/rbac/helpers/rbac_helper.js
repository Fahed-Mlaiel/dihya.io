// rbac_helper.js
// Helper RBAC (JS)
function validateRole(role) {
  return typeof role === 'string' && role.length > 0;
}
module.exports = { validateRole };
