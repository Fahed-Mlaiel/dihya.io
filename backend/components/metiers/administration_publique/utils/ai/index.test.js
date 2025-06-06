// index.test.js – Test d'intégration du point d'entrée AI JS
const ai = require('./index');
describe('Entrée JS AI utils threed', () => {
  it('doit exposer aiFallback', () => {
    expect(ai).toHaveProperty('aiFallback');
  });
});
