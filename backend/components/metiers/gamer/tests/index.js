// Point d'entrée JS pour les tests Gamer
module.exports = {
  testApi: require('./test_api.py'),
  testLegacy: require('./test_legacy.py'),
  testPlugins: require('./test_plugins.py'),
  testServices: require('./test_services.py'),
  testTemplates: require('./test_templates.py'),
  testUtils: require('./test_utils.py'),
  sampleTest: require('./sample_test.py')
};
