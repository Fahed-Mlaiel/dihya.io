// Point d’entrée JS pour core services
module.exports = {
  serviceThreed: require('./impl/service_threed'),
  servicesController: require('./controllers/services_controller'),
  servicesHelper: require('./helpers/services_helper'),
  apiService: require('./api/api_service'),
};
