// __init__.test.js – Test d’intégration du point d’entrée JS core templates
const entry = require('./__init__');
describe('Entrée JS core templates', () => {
  it('doit exposer templateThreed', () => {
    expect(entry).toHaveProperty('templateThreed');
  });
});
