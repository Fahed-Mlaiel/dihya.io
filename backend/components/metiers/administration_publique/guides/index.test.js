// index.test.js – Test d’intégration du point d’entrée index.js des guides Threed
const entry = require('./index.js');
describe('Entrée index.js guides Threed', () => {
  it('existe et peut être importée', () => {
    expect(entry).toBeDefined();
  });
});
