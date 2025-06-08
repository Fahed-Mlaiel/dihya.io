// Point d’entrée principal JS pour scripts

module.exports = {
  audit: require('./audit'),
  backup: require('./backup'),
  compliance: require('./compliance'),
  restore: require('./restore')
};
