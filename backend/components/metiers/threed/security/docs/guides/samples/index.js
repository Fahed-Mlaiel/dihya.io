// index.js – Point d'entrée modulaire des samples guides sécurité 3D
// Permet l'import centralisé de tous les exemples avancés (api, audit, compliance, monitoring, onboarding, rbac, faq)

const api = require('./api');
const audit = require('./audit');
const compliance = require('./compliance');
const monitoring = require('./monitoring');
const onboarding = require('./onboarding');
const rbac = require('./rbac');
const faq = require('./faq');

module.exports = {
  api,
  audit,
  compliance,
  monitoring,
  onboarding,
  rbac,
  faq
};
