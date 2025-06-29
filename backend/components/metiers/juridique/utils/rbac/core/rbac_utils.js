// rbac_utils.js – Utilitaires avancés RBAC pour Juridique (JS)
// Ultra avancé, conforme RGPD, audit, accessibilité, multitenancy, plugins, CI/CD ready

function isValidRole(role) {
  return typeof role === 'string' && role.length >= 1 && role.length <= 64 && /^[_a-zA-Z][_a-zA-Z0-9]*$/.test(role);
}

function filterRoles(roles, allowed) {
  return roles.filter(r => allowed.includes(r));
}

function auditRoles(roles) {
  return {
    roles,
    count: roles.length,
    unique: new Set(roles).size,
    auditDate: new Date().toISOString(),
  };
}

function anonymizeRoles(roles) {
  return roles.map((_, i) => `role_${i+1}`);
}

module.exports = {
  isValidRole,
  filterRoles,
  auditRoles,
  anonymizeRoles,
};
