// index.js – Point d’entrée principal JS patterns
// Import/export de tous les modules et blueprints JS du dossier

module.exports = {
  webApp: require('./webApp'),
  backendApi: require('./backendApi'),
  mobileApp: require('./mobileApp'),
  plugin: require('./plugin'),
  analytics: require('./analytics'),
  seoService: require('./seoService'),
  authService: require('./authService'),
  roles: require('./roles'),
  permissions: require('./permissions'),
  notificationService: require('./notificationService'),
  middleware: require('./middleware'),
  validators: require('./validators'),
  crypto: require('./crypto'),
  rgpd: require('./rgpd'),
  audit: require('./audit'),
  monitoring: require('./monitoring'),
  scheduler: require('./scheduler'),
  migration: require('./migration'),
  autoGenerate: require('./autoGenerate'),
  module_utils: require('./module_utils'),
};
