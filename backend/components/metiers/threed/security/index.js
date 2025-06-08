// Point d’entrée principal JS pour le module de sécurité

module.exports = {
  assets: require('./assets'),
  audit: require('./audit'),
  compliance: require('./compliance'),
  core: require('./core'),
  docs: require('./docs'),
  helpers: require('./helpers'),
  monitoring: require('./monitoring'),
  policy: require('./policy'),
  rbac: require('./rbac'),
  samples: require('./samples'),
  scripts: require('./scripts'),
  validators: require('./validators')
};
