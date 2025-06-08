// index.js
// Point d’entrée principal pour tous les modules de samples sécurité (clé en main)

const access = require('./access');
const audit = require('./audit');
const compliance = require('./compliance');
const monitoring = require('./monitoring');
const onboarding = require('./onboarding');
const rbac = require('./rbac');
const rgpd = require('./rgpd');

module.exports = {
  access,
  audit,
  compliance,
  monitoring,
  onboarding,
  rbac,
  rgpd
};

// Utilisation :
// const samples = require('./index');
// samples.access.generateMfaToken(...)
// samples.audit.logAuditEvent(...)
// ...
