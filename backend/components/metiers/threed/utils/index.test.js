// index.test.js – Test d'intégration du point d'entrée JS
const utils = require('./index');
describe('Entrée JS utils threed', () => {
  it('doit exposer les utilitaires principaux', () => {
    expect(utils).toHaveProperty('aiFallback');
    expect(utils).toHaveProperty('auditThreed');
    expect(utils).toHaveProperty('exportToJSON');
    expect(utils).toHaveProperty('utils_helper');
    expect(utils).toHaveProperty('translate');
    expect(utils).toHaveProperty('logInfo');
    expect(utils).toHaveProperty('metrics');
    expect(utils).toHaveProperty('pluginManager');
    expect(utils).toHaveProperty('check_permission');
    expect(utils).toHaveProperty('validators');
    expect(utils).toHaveProperty('views');
  });
});
