// index.js – Point d'entrée modulaire des guides sécurité 3D
// Permet l'import centralisé de tous les guides thématiques (api, audit, compliance, monitoring, onboarding, rbac, faq, samples)

const api = require('./api');
const audit = require('./audit');
const compliance = require('./compliance');
const monitoring = require('./monitoring');
const onboarding = require('./onboarding');
const rbac = require('./rbac');
const faq = require('./faq');
const samples = require('./samples');

module.exports = {
  api,
  audit,
  compliance,
  monitoring,
  onboarding,
  rbac,
  faq,
  samples
};
