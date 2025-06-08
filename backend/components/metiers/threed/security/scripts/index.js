// Point d’entrée principal du module scripts de sécurité
module.exports = {
  audit: require('./audit'),
  backup: require('./backup'),
  compliance: require('./compliance'),
  restore: require('./restore'),
  samples: require('./samples')
};
