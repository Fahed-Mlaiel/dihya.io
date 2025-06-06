// index.test.js – Test d'intégration du point d'entrée logger JS
const logger = require('./index');
describe('Entrée JS logger utils threed', () => {
  it('doit exposer logInfo et logError', () => {
    expect(logger).toHaveProperty('logInfo');
    expect(logger).toHaveProperty('logError');
  });
});
