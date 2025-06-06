// sample_utils.js – Exemples ultra avancés d’utilitaires pour tests, audit, conformité, RGPD
const { generateId, auditLog } = require('../utils/core/core_utils');
const { translate } = require('../utils/i18n/i18n_utils');
const { hasPermission } = require('../utils/rbac/rbac_utils');

function sampleUser() {
  return {
    id: generateId('user'),
    username: 'sampleuser',
    email: 'sample@dihya.io',
    roles: ['admin', 'auditor']
  };
}

function sampleAuditAction() {
  const user = sampleUser();
  return auditLog('SAMPLE_ACTION', user.id, { lang: translate('audit', 'fr') });
}

function samplePermissionCheck() {
  const user = sampleUser();
  return hasPermission(user, 'audit');
}

module.exports = {
  sampleUser,
  sampleAuditAction,
  samplePermissionCheck
};
