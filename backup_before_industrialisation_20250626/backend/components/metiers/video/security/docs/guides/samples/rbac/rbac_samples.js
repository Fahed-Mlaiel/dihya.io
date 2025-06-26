// rbac_samples.js – Exemples RBAC (Node.js)
function sampleRoleModel() {
  return { role: 'admin', permissions: ['read', 'write', 'delete'] };
}
module.exports = { sampleRoleModel };
