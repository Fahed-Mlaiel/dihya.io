// Point d’entrée pour l’export/import de tous les blueprints IA
module.exports = {
  webApp: require('./webApp'),
  backendApi: require('./backendApi'),
  mobileApp: require('./mobileApp'),
  plugin: require('./plugin'),
  custom: require('./custom_blueprint'),
};
