// index.js
// Point d'entrée principal JS pour le module core services threed.
// Permet l'import centralisé de tous les sous-modules (api, controllers, helpers, impl, samples).

module.exports = {
  ApiService: require('./api/api_service'),
  ServicesController: require('./controllers/services_controller'),
  ServicesHelper: require('./helpers/services_helper'),
  ServiceThreed: require('./impl/service_threed'),
  SampleService: require('./samples/sample_service'),
};
