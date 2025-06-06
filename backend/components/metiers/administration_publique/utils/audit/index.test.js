// index.test.js – Test d'intégration du point d'entrée audit JS
const audit = require('./index');
describe('Entrée JS audit utils threed', () => {
  it('doit exposer auditThreed', () => {
    expect(audit).toHaveProperty('auditThreed');
  });
});
